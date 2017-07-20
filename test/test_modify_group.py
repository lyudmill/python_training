from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    old_groups = app.group.get_group_list()
    group = Group(name="Modified group")
    group.id = old_groups[0].id
    app.group.modify_first_group(Group(name="Modified group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    old = sorted(old_groups, key=Group.id_or_max)
    new = sorted(new_groups, key=Group.id_or_max)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group"))
    old_groups = app.group.get_group_list()
    group = Group(name="Modified group")
    group.id = old_groups[0].id
    app.group.modify_first_group(Group(header="modified header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
