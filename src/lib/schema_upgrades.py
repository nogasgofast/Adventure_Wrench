
from pony.orm import *

def upgrade_db(exception, file_path):
    if f"{exception}" == "no such column: Active.isAlarm":
        print("Trying database upgrade from v2.0-v2.1")
        from lib.migrations.two_point_zero_to_two_point_one import database_factory
        db = database_factory()
        try:
            db.bind(provider="sqlite",
                       filename=file_path,
                       create_db=False)
            db.generate_mapping(create_tables=False)
        except pony.orm.dbapiprovider.OperationalError as e:
            print(f"Falling back to deeper upgrades")
            # detected an even older database then i thought! attempting more upgrades! MORE!
            del(db)
            upgrade_db(e, file_path)
            upgrade_db(exception, file_path)
            return
        with db_session:
            db.execute('alter table Active add column isAlarm boolean;')
        del(db)
    elif f"{exception}" == "no such table: Settings":
        print("Trying database upgrade from v1.2-v2.0")
        from lib.migrations.one_point_two_to_two_point_zero import database_factory
        db = database_factory()
        db.bind(provider="sqlite",
                   filename=file_path,
                   create_db=False)
        db.generate_mapping(create_tables=True)
        with db_session:
            db.Settings(name="pnp_system_name", value="5e")
        del(db)
