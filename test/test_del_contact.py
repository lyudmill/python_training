import time
from model.contact import Contact


def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact())
    old_list = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    app.open_home_page()
    time.sleep(10)
    new_list=app.contact.get_contacts_list()
    assert len(old_list)-1 == len(new_list)
    old_list[0:1]=[]
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
