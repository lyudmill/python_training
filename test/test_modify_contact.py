from model.contact import Contact
import time
import random


#@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_modify_some_contact_name(app, json_mod_contacts):
    contact = json_mod_contacts
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Sergey", midname="Alex", lastname="Sergeev", nickname="Serg"))
        time.sleep(10)
    old_list = app.contact.get_contacts_list()
    index = random.randrange(len(old_list))
    app.contact.modify_contact_by_index(index, contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list) == len(new_list)
    old_list[index].firstname = contact.firstname
    old_list[index].lastname = contact.lastname
    old_list[index].midname = contact.midname
    old_list[index].nickname = contact.nickname
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
