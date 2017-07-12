from model.contact import Contact


def test_edit_first_contact(app):
    app.open_home_page()
    app.contact.edit_first_contact(Contact(firstname="Sergey", midname="S.", lastname="Sergeev", nickname="Serg",
                       title="Manager", company="Big_company_pro", street="Lenina Street,77",
                       homephone="+7(812)77777", mobilephone="+7(911)77777", workphone="+7(812)3333337",
                       email="sergey.sergeev.big_company.com", email2="iva.ivanov@big_company_pro.com",
                       byear="1991", homepage="www.sergeev.com", address2="new_adr",
                       notes="Some comments"))
    app.open_home_page()


