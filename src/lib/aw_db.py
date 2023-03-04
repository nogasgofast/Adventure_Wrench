from pony.orm import *

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
    name = Required(str)
    is_folder = Optional(bool, default=False)
    over = Optional('Templates', reverse='under')
    under = Set('Templates', reverse='over')
    vault = Set('Vault', reverse='templates')
    lore = Set('Lore')
    attributes = Set('Attributes', reverse='template')
    items = Set('Items', reverse='template')
    actions = Set('Actions', reverse='template')
    stats = Set('Stats', reverse='template')
    rtables = Set('Rtables', reverse='used_in_templates')
    rtable_items = Set('Rtable_items')

class Lore(aw_db.Entity):
    name = Optional(str)
    description = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtable_items')
    def to_strings(self):
        return (f'{self.name}:\n'
                f'    {self.description}')

class Stats(aw_db.Entity):
    name = Optional(str)
    description = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtable_items')
    def to_strings(self):
        return f'{self.name}: {self.description}'

class Attributes(aw_db.Entity):
    name = Optional(str)
    content = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtable_items')
    def to_strings(self):
        return f'{self.name}: {self.content}'

class Items(aw_db.Entity):
    name = Optional(str)
    weight = Optional(str)
    quantity = Optional(int)
    description = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtable_items')
    def to_strings(self):
        return (f'{self.name}:\n'
                f'    {self.description}')

class Actions(aw_db.Entity):
    name = Optional(str)
    cost = Optional(str)
    limitations = Optional(str)
    result = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtable_items')
    def to_strings(self):
        return (f'{self.name}:\n'
                f'    cost: {self.cost}\n'
                f'    limitations: {self.limitations}\n\n'
                f'    {self.result}')

class Rtables(aw_db.Entity):
    name = Optional(str)
    isRandom = Required(bool, default=False)
    immutable = Required(bool, default=True)
    diceRoll = Optional(str)
    items = Set('Rtable_items', reverse='table')
    used_in_templates = Set('Templates')
    used_in_rtable_items = Set('Rtable_items', reverse='rtable')
    def to_strings(self):
        items = []
        for i in self.items:
            items.append(i.to_strings())
        return f'{self.name}: {self.diceRoll}\n' + ''.join(sorted(items))

class Rtable_items(aw_db.Entity):
    table = Required('Rtables')
    match = Optional(str)
    lore = Optional('Lore', reverse='rtable_items')
    attribute = Optional('Attributes', reverse='rtable_items')
    stat = Optional('Stats', reverse='rtable_items')
    item = Optional('Items', reverse='rtable_items')
    action = Optional('Actions', reverse='rtable_items')
    template = Optional('Templates', reverse='rtable_items')
    rtable = Optional('Rtables', reverse='used_in_rtable_items')
    def to_strings(self):
        if self.lore:
            thing = self.lore
        if self.attribute:
            thing = self.attribute
        if self.stat:
            thing = self.stat
        if self.item:
            thing = self.item
        if self.action:
            thing = self.action
        if self.rtable:
            thing = rtable
        thing = thing.to_strings()
        return f'    {self.match}: {thing}\n'


if __name__ == '__main__':
    try:
        aw_db.bind("sqlite", ":memory:", create_db=True)
        aw_db.generate_mapping(create_tables=True)
        print("schema syntax: OKAY")
    except:
        print("schema syntax: FAIL")
        raise
