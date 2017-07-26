import re
from model.contact import Contact
from random import randrange

def test_contact_info_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails == merge_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phones_as_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.homepage == contact_from_edit_page.homepage


def clear(s):
    return re.sub("[()\- ]","", s)

def merge_phones_as_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
            map(lambda x: clear(x),
                filter(lambda x: x is not None,
                    [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                           filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3])))
