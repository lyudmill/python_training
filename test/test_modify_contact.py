from model.contact import Contact

def test_modify_first_contact_name(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Sergey", midname="S.", lastname="Sergeev", nickname="Serg"))
    app.contact.modify_first_contact(Contact(firstname="Andrey", midname="A.", lastname="Andreev", nickname="Andy"))
    app.open_home_page()


def test_modify_first_contact_job(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Sergey", midname="S.", lastname="Sergeev", nickname="Serg",
                                   title="Manager", company="Big_company_pro", street="Lenina Street,77"))
    app.contact.modify_first_contact(Contact(title="Senior Mng", company="Very_big_company", street="Central St.,777"))
    app.open_home_page()
