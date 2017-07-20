# -*- coding: utf-8 -*-
import time
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    old_list = app.contact.get_contacts_list()
    new_contact = Contact(firstname="Ivan", midname="I.", lastname="Ivanov", nickname="Vanya",
                       title="Tester", company="Big_company", street="Lenina Street",
                       homephone="+7(812)9999999", mobilephone="+7(911)9999999", workphone="+7(812)3333333",
                       email="iva.ivanov.big_company.com", email2="iva.ivanov@big_company.com",
                       byear="1990", homepage="www.ivanivanov.com", address2="addressss",
                       notes="No comments")
    app.contact.open_contact_page()
    app.contact.create(new_contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list)+1 == len(new_list)
    old_list.append(new_contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)



def test_add_empty_contact(app):
    app.open_home_page()
    old_list = app.contact.get_contacts_list()
    new_contact = Contact(firstname="", midname="", lastname="", nickname="",
                       title="", company="", street="",
                       homephone="", mobilephone="", workphone="",
                       email="", email2="",
                       byear="", homepage="", address2="",
                       notes="")
    app.contact.open_contact_page()
    app.contact.create(new_contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list)+1 == len(new_list)
    old_list.append(new_contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)


