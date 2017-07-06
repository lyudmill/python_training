# -*- coding: utf-8 -*-
import time
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.create(Contact(firstname="Ivan", midname="I.", lastname="Ivanov", nickname="Vanya",
                       title="Tester", company="Big_company", street="Lenina Street",
                       homephone="+7(812)9999999", mobilephone="+7(911)9999999", workphone="+7(812)3333333",
                       email="iva.ivanov.big_company.com", email2="iva.ivanov@big_company.com",
                       byear="1990", homepage="www.ivanivanov.com", address2="addressss",
                       notes="No comments"))
    app.open_home_page()
    time.sleep(3)
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.create(Contact(firstname="", midname="", lastname="", nickname="",
                       title="", company="", street="",
                       homephone="", mobilephone="", workphone="",
                       email="", email2="",
                       byear="", homepage="", address2="",
                       notes=""))
    app.open_home_page()
    time.sleep(3)
    app.session.logout()

