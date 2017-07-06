import time
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="Edited group", header="Edited header", footer="Edited footer"))
    app.group.open_groups_page()
    time.sleep(3)
    app.session.logout()