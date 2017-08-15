import time
from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact())
    old_list = db.get_contacts_list()
    contact = random.choice(old_list)
    app.contact.delete_contact_by_id(contact.id)
    new_list = db.get_contacts_list()
    old_list.remove(contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_list, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

