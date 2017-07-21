import time
from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact())
    old_list = app.contact.get_contacts_list()
    index = randrange(len(old_list))
    app.contact.delete_contact_by_index(index)
    app.open_home_page()
    time.sleep(10)
    assert len(old_list)-1 == app.contact.count()
    new_list = app.contact.get_contacts_list()
    old_list[index:index + 1] = []
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)

def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact())
        time.sleep(5)
    old_list = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    app.open_home_page()
    time.sleep(10)
    assert len(old_list)-1 == app.contact.count()
    new_list=app.contact.get_contacts_list()
    old_list[0:1]=[]
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
