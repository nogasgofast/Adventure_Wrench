from pony.orm import *

aw_db = Database()

class Players(aw_db.Entity):
    name = Optional(str)
    description = Optional(str)
    initiative = Optional(int)
    hp = Optional(int)

class Current_encoutner(aw_db.Entity):
    content = Required(str)

class Templates(aw_db.Entity):
    name = Required(str)
    over = Set('Templates', reverse='under')
    under = Set('Templates', reverse='over')
    vault_stuff = Set('Vault_stuff', reverse='templates')
    description = Set('Descriptions', reverse='templates')
    attributes = Set('Attributes', reverse='templates')
    items = Set('Items', reverse='templates')
    actions = Set('Actions', reverse='templates')
    stats = Set('Stats', reverse='templates')

class Descriptions(aw_db.Entity):
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
    type = Required('Rtype')
    name = Optional(str)
    content = Optional(str)

class Rtype(aw_db.Entity):
    name = Required(str)
    rtables = Set('Rtables')

class Vault_stuff(aw_db.Entity):
    name = Required(str)
    content = Optional(str)
    templates = Set('Templates', reverse='vault_stuff')


if __name__ == '__main__':
    try:
        aw_db.bind("sqlite", ":memory:", create_db=True)
        aw_db.generate_mapping(create_tables=True)
        with db_session:
            aw_db.Rtype(name='Roll table')
            aw_db.Rtype(name='Random table')
            aw_db.Rtype(name='table')
        print("schema syntax: OKAY")
    except:
        print("schema syntax: FAIL")
        raise
