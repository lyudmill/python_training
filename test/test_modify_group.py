from model.group import Group
import random
import pytest
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name=random_string("mod_name", 7), header=random_string("mod_header", 15), footer=random_string("mod_footer", 12))
            for i in range(3)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])


def test_modify_group(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name="New group"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

