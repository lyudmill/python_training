from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    old_groups = app.group.get_group_list()
    group = Group(name="Modified group")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name = old_groups[index].name, gr_id = old_groups[index].id, header="Modified header")
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
