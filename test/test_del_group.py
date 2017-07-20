from model.group import Group


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="name for delete"))
        app.group.return_to_groups_page()
    app.group.delete_first_group()
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) -1 == len(new_groups)
    old_groups[0:1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
