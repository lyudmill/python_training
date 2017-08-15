from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, ormdb, check_ui):
    group_list = ormdb.get_group_list()
    #select group
    if len(group_list) == 0:
        app.group.create(Group(name="New group"))
        group_list = ormdb.get_group_list()
    group = random.choice(group_list)
    #get contacts in group
    contacts_in_group = ormdb.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        # select contact
        contact_list = ormdb.get_contacts_list()
        if len(contact_list) == 0:
            app.contact.create(
                app.contact.create(Contact(firstname="Sergey", midname="Alex", lastname="Sergeev", nickname="Serg")))
            contact_list = ormdb.get_contacts_list()
        contact = random.choice(contact_list)
        app.contact.add_contact_to_group(contact, group)
        contacts_in_group = ormdb.get_contacts_in_group(group)
    else:
        #select group
        app.contact.select_group(group)
    #delete from group
    contact_to_delete=random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact_to_delete)
    #verify
    new_contacts_in_group = ormdb.get_contacts_in_group(group)
    contacts_in_group.remove(contact_to_delete)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

