# -*- coding: utf-8 -*-
from model.group import Group


#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups,key=Group.id_or_max) ==sorted(new_groups,key=Group.id_or_max)
    if check_ui:
        assert len(old_groups) == app.group.count()
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        print("***UI OK**")
