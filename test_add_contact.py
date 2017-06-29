# -*- coding: utf-8 -*-
import time
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_contact_page()
    app.create_new_contact(Contact(firstname="Ivan", midname="I.", lastname="Ivanov", nickname="Vanya",
                                        title="Tester", company="Big_company", street="Lenina Street",
                                        homephone="+7(812)9999999", mobilephone="+7(911)9999999", workphone="+7(812)3333333",
                                        email="iva.ivanov.big_company.com",email2="iva.ivanov@big_company.com",
                                        byear="1990", homepage="www.ivanivanov.com", address2="addressss",
                                        notes="No comments"))
    app.open_home_page()
    time.sleep(3)
    app.logout()

def test_add_empty_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_contact_page()
    app.create_new_contact(Contact(firstname="", midname="", lastname="", nickname="",
                                        title="", company="", street="",
                                        homephone="", mobilephone="", workphone="",
                                        email="",email2="",
                                        byear="", homepage="", address2="",
                                        notes=""))
    app.open_home_page()
    time.sleep(3)
    app.logout()

