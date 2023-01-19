from pony.orm import *

aw_db = Database()

class Active(aw_db.Entity):
    name = Optional(str, default=' *** ')
    description = Optional(str, default='')
    initiative = Optional(int, default=1)
    hp = Optional(int, default=1)
    max_hp = Optional(int, default=1)
    group_hp = Optional(IntArray)
    count = Optional(int, default=1)
    death_save_fail = Optional(int, default=0)
    death_save_success = Optional(int, default=0)
    black_star = Optional(int, default=0)
    white_star = Optional(int, default=0)
    type = Required(str)

class Vault(aw_db.Entity):
    name = Optional(str, default=' *** ')
    description = Optional(str, default='')
    initiative = Optional(int, default=1)
    hp = Optional(int, default=1)
    max_hp = Optional(int, default=1)
    group_hp = Optional(IntArray)
    count = Optional(int, default=1)
    templates = Set('Templates', reverse='vault')
    type = Required(str)

class Templates(aw_db.Entity):
    name = Required(str)
    over = Optional('Templates', reverse='under')
    under = Set('Templates', reverse='over')
    vault = Set('Vault', reverse='templates')
    lore = Set('Lore')
    attributes = Set('Attributes', reverse='template')
    items = Set('Items', reverse='template')
    actions = Set('Actions', reverse='template')
    stats = Set('Stats', reverse='template')
    rtables = Set('Rtables', reverse='template')
    rtable_items = Set('Rtables_items')

class Lore(aw_db.Entity):
    name = Optional(str)
    description = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtables_items')

class Stats(aw_db.Entity):
    name = Optional(str)
    description = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtables_items')

class Attributes(aw_db.Entity):
    name = Optional(str)
    content = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtables_items')

class Items(aw_db.Entity):
    name = Optional(str)
    weight = Optional(str)
    quantity = Optional(int)
    description = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtables_items')

class Actions(aw_db.Entity):
    name = Optional(str)
    cost = Optional(str)
    limitations = Optional(str)
    result = Optional(str)
    template = Required('Templates')
    rtable_items = Set('Rtables_items')

class Rtables(aw_db.Entity):
    name = Optional(str)
    isRandom = Required(bool)
    diceRoll = Optional(str)
    items = Set('Rtables_items', reverse='table')
    template = Set('Templates')
    over = Set('Rtables_items', reverse='rtable')

class Rtables_items(aw_db.Entity):
    table = Required('Rtables')
    match = Optional(str)
    lore = Optional('Lore', reverse='rtable_items')
    attribute = Optional('Attributes', reverse='rtable_items')
    stat = Optional('Stats', reverse='rtable_items')
    item = Optional('Items', reverse='rtable_items')
    action = Optional('Actions', reverse='rtable_items')
    template = Optional('Templates', reverse='rtable_items')
    rtable = Optional('Rtables', reverse='over')


if __name__ == '__main__':
    try:
        aw_db.bind("sqlite", ":memory:", create_db=True)
        aw_db.generate_mapping(create_tables=True)
        with db_session:
            aw_db.Vault(name='group 3', group_hp=[1,2,3],
                        hp=6, max_hp=6, count=3, type='creature')
            aw_db.Vault(name='c1', group_hp='',
                        hp=6, max_hp=20, count=1, type='creature')
            aw_db.Vault(name='c2', group_hp='',
                        hp=6, max_hp=6, count=1, type='creature')
            aw_db.Vault(name='group 1', group_hp=[1,2,3,4],
                        hp=6, max_hp=40, count=4, type='creature')
            aw_db.Active(type='pc')
            aw_db.Active(type='creature')
            aw_db.Active(type='npc')
            aw_db.Active(type='trap')
        print("schema syntax: OKAY")
    except:
        print("schema syntax: FAIL")
        raise
