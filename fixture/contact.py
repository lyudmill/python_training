from model.contact import Contact


class ContactHelper:
    contact_cash = None

    def __init__(self,app):
        self.app =  app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cash = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cash = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        #select first contack
        wd.find_elements_by_name("selected[]")[index].click()
        #click on "Delete"
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #Confirm
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        #select first contack
        return len(wd.find_elements_by_name("selected[]"))

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.midname)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.street)
        self.change_field("home", contact.homephone)
        self.change_field("mobile", contact.mobilephone)
        self.change_field("work", contact.workphone)
        self.change_field("email", contact.email)
        self.change_field("email", contact.email2)
        self.change_field("byear", contact.byear)
        self.change_field("homepage", contact.homepage)
        self.change_field("address2", contact.address2)
        self.change_field("notes", contact.notes)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_contacts_list(self):
        wd = self.app.wd
        if self.contact_cash is None:
            self.contact_cash = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                emails=cells[3].text
                phones=cells[4].text
                self.contact_cash.append(Contact(firstname=first_name, lastname=last_name, id=id, email=emails, workphone= phones))
        return list(self.contact_cash)