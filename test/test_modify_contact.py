from model.contact import Contact
import time
import random
import pytest
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
            Contact(firstname=random_string("m_first", 10), midname=random_string("mid", 10),
                lastname=random_string("m_last", 10),
                address=random_string("m_adr1", 30),
                homephone=random_phone(), mobilephone=random_phone(), workphone=random_phone(),
                email=random_email(), email2=random_email(),
                homepage=random_homepage() , address2=random_string("m_adr2", 30))
            for i in range(3)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_modify_some_contact_name(app, contact):
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


def atest_modify_first_contact_job(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Sergey", midname="S.", lastname="Sergeev", nickname="Serg",
                                   title="Manager", company="Big_company_pro", address="Lenina Street,77"))
    old_list = app.contact.get_contacts_list()
    new_contact=Contact(title="Senior Mng", company="Very_big_company", address="Central St.,777")
    app.contact.modify_first_contact(new_contact)
    app.open_home_page()
    new_list=app.contact.get_contacts_list()
    assert len(old_list) == len(new_list)
    old_list[0].title = new_contact.title
    old_list[0].company = new_contact.company
    old_list[0].street = new_contact.address
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)
