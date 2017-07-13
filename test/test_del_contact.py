from model.contact import Contact

def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.create(Contact())
    app.contact.delete_first_contact()
    app.open_home_page()
