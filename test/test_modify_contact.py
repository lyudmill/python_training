from model.contact import Contact

def test_modify_first_contact_name(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Sergey", midname="S.", lastname="Sergeev", nickname="Serg"))
    old_list = app.contact.get_contacts_list()
    new_contact=Contact(firstname="Andrey", midname="A.", lastname="Andreev", nickname="Andy")
    app.contact.modify_first_contact(new_contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list) == len(new_list)
    old_list[0].firstname = new_contact.firstname
    old_list[0].lastname = new_contact.lastname
    old_list[0].midname = new_contact.midname
    old_list[0].nickname = new_contact.nickname
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)


def test_modify_first_contact_job(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Sergey", midname="S.", lastname="Sergeev", nickname="Serg",
                                   title="Manager", company="Big_company_pro", street="Lenina Street,77"))
    old_list = app.contact.get_contacts_list()
    new_contact=Contact(title="Senior Mng", company="Very_big_company", street="Central St.,777")
    app.contact.modify_first_contact(new_contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list) == len(new_list)
    old_list[0].title = new_contact.title
    old_list[0].company = new_contact.company
    old_list[0].street = new_contact.street
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
