import time
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Modified group"))
    time.sleep(3)


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="modified header"))
    time.sleep(3)
