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
    lore = Set('Lore', reverse='templates')
    attributes = Set('Attributes', reverse='templates')
    items = Set('Items', reverse='templates')
    actions = Set('Actions', reverse='templates')
    stats = Set('Stats', reverse='templates')

class Lore(aw_db.Entity):
    name = Optional(str)
    content = Optional(str)
    templates = Set('Templates')

class Stats(aw_db.Entity):
    name = Optional(str)
    content = Optional(str)
    templates = Set('Templates')

class Attributes(aw_db.Entity):
    name = Optional(str)
    content = Optional(str)
    templates = Set('Templates')

class Items(aw_db.Entity):
    name = Optional(str)
    weight = Optional(int)
    content = Optional(str)
    templates = Set('Templates')

class Actions(aw_db.Entity):
    name = Optional(str)
    content = Optional(str)
    templates = Set('Templates')

class Rtables(aw_db.Entity):
    type = Required(str)
    name = Optional(str)
    content = Optional(str)


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
