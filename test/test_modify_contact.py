from model.contact import Contact
import time
import random


#@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_modify_some_contact_name(app, db, check_ui, json_mod_contacts):
    contact = json_mod_contacts
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Sergey", midname="Alex", lastname="Sergeev", nickname="Serg"))
    old_list = db.get_contacts_list()
    selected_contact = random.choice(old_list)
    index = old_list.index(selected_contact)
    contact.id = selected_contact.id
    app.contact.modify_contact_by_id(contact)
    new_list=db.get_contacts_list()
    assert len(old_list) == len(new_list)
    old_list[index]=contact
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_list, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
        print("Check_ui OK")