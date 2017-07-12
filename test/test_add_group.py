# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="new group", header="new group header", footer="footer"))
    app.group.open_groups_page()

def test_add_empty_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.open_groups_page()

