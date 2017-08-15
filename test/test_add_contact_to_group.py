from model.contact import Contact
from model.group import Group
import random


def _test_add_contact_to_group(app, ormdb, check_ui):
    #select contact
    contact_list = ormdb.get_contacts_list()
    if len(contact_list) == 0:
        app.contact.create(app.contact.create(Contact(firstname="Sergey", midname="Alex", lastname="Sergeev", nickname="Serg")))
        contact_list = ormdb.get_contacts_list()
    contact = random.choice(contact_list)
    group_list = ormdb.get_group_list()
    #select group
    if len(group_list) == 0:
        app.group.create(Group(name="New group"))
        group_list = ormdb.get_group_list()
    group = random.choice(group_list)
    contacts_in_group = ormdb.get_contacts_in_group(group)
    #add contact to group
    app.contact.add_contact_to_group(contact, group)
    #verify
    new_contacts_in_group = ormdb.get_contacts_in_group(group)
    contacts_in_group.append(contact)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


