# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    app.open_home_page()
    old_list = app.contact.get_contacts_list()
    app.contact.open_contact_page()
    app.contact.create(contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list)+1 == len(new_list)
    old_list.append(contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)


