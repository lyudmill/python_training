import time


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.open_home_page()
    time.sleep(3)
    app.session.logout()
