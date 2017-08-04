# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    prefix = random.choice(["",
                            "+7(%s)" % "".join([random.choice(string.digits) for i in range(3)]),
                            "8%s" % "".join([random.choice(string.digits) for i in range(4)])
    ])
    return prefix + "".join([random.choice(string.digits) for i in range(7)])


def random_email():
    return "%s@%s.%s" %(random_string("",15), random_string("",10), random.choice(["com","ru","de"]))


def random_homepage():
    return random.choice([None] +
                         ["www.%s.%s" %(random_string("",15), random.choice(["com","ru","de"])) for i in range(3)])


test_data = [Contact(firstname="", midname="", lastname="", address="",
                homephone="", mobilephone="", workphone="",
                email="", email2="",homepage="", address2="")] + [
            Contact(firstname=random_string("first", 10), midname=random_string("mid", 10),
                lastname=random_string("last", 10),
                address=random_string("adr1", 30),
                homephone=random_phone(), mobilephone=random_phone(), workphone=random_phone(),
                email=random_email(), email2=random_email(),
                homepage=random_homepage() , address2=random_string("adr2", 30))
            for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    app.open_home_page()
    old_list = app.contact.get_contacts_list()
    app.contact.open_contact_page()
    app.contact.create(contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list)+1 == len(new_list)
    old_list.append(contact)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)


