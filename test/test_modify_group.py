from model.group import Group
import random


def test_modify_group(app, db, check_ui, json_mod_groups):
    group = json_mod_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    old_groups = db.get_group_list()
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    old_groups[index]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

