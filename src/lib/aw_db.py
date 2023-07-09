from pony.orm import *


def database_factory():
    aw_db = Database()
    class Active(aw_db.Entity):
        name = Optional(str, default='* * *')
        stat_block = Optional(str, default='')
        initiative = Optional(int, default=1)
        hp = Optional(int, default=1)
        max_hp = Optional(int, default=1)
        group_hp = Optional(IntArray)
        count = Optional(int, default=1)
        death_save_fail = Optional(int, default=0)
        death_save_success = Optional(int, default=0)
        black_star = Optional(int, default=0)
        white_star = Optional(int, default=0)
        player = Required(bool, default=False)
        from_vault = Optional('Vault', reverse='in_active')

    class Vault(aw_db.Entity):
        name = Optional(str, default='* * *')
        initiative = Optional(int, default=1)
        hp = Optional(int, default=1)
        max_hp = Optional(int, default=1)
        group_hp = Optional(IntArray)
        stat_block = Optional(str, default='')
        ability_str = Optional(int, default=10)
        ability_dex = Optional(int, default=10)
        ability_con = Optional(int, default=10)
        ability_int = Optional(int, default=10)
        ability_wis = Optional(int, default=10)
        ability_cha = Optional(int, default=10)
        cr = Optional(int, default=1)
        count = Optional(int, default=1)
        templates = Set('Templates', reverse='vault')
        in_active = Set('Active', reverse='from_vault')

    class Templates(aw_db.Entity):
        'all types of details.'
        vault = Set('Vault', reverse='templates')
        over_me = Set('Templates', reverse='under_me')
        under_me = Set('Templates', reverse='over_me')
        name = Optional(str)
        # lore, stat, attribute, item, action, rtable, template
        detail_type = Required(str)
        rtable_over_me = Set('Rtable_items', reverse='table_item')
        description = Optional(str)
        weight = Optional(str)
        quantity = Optional(int, default=1)
        cost = Optional(str)
        limitations = Optional(str)
        result = Optional(str)
        is_random = Optional(bool, default=False)
        onlyPrint = Optional(bool, default=True)
        dice_roll = Optional(str)
        # This is how to go up the tree
        roll_table_items = Set('Rtable_items', reverse='rtable')
        # templates
        is_folder = Optional(bool, default=False)
        def to_display(self):
            match self.detail_type:
                case 'lore' | 'item':
                    # print("returning lore or item")
                    return (f'{self.name}:\n'
                            f'    {self.description}')
                case 'stat' | 'attribute':
                    return f'{self.name}: {self.description}'
                case 'action':
                    return (f'=[{self.name}]=:\n'
                            f'    cost: {self.cost}\n'
                            f'    limitations: {self.limitations}\n    ' +
                            '\n    '.join(self.result.split('\n')))

    class Rtable_items(aw_db.Entity):
        # table for going up tree
        rtable = Required('Templates', reverse='roll_table_items')
        match = Optional(str)
        # and as you might guess going down the tree
        table_item = Optional('Templates', reverse='rtable_over_me')
    return aw_db


if __name__ == '__main__':
    aw_db = database_factory()
    try:
        aw_db.bind("sqlite", ":memory:", create_db=True)
        aw_db.generate_mapping(create_tables=True)
        print("schema syntax: OKAY")
    except:
        print("schema syntax: FAIL")
        raise
