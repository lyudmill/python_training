from model.group import Group
from random import randrange

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name for delete"))
        app.group.return_to_groups_page()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) -1 == len(new_groups)
    old_groups[0:1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name for delete"))
        app.group.return_to_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) -1 == len(new_groups)
    old_groups[index:index+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)