from model.group import Group
from timeit import timeit


def test_orm(app, ormdb):
    db_list = ormdb.get_group_list()
    print(db_list)
    print(ormdb.get_contacts_list())
    print(ormdb.get_contacts_in_group(db_list[0]))




def _test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return(Group(gr_id = group.id, name = group.name.strip().replace("  ", " ")))
        print(timeit(lambda: map(clean, db.get_group_list()), number=1000))

    assert False #sorted(ui_list, key = Group.id_or_max) == sorted(db_list, key = Group.id_or_max)