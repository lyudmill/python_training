from model.contact import Contact
import re

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
        wd.find_element_by_name("submit").click()
        #wd.find_element_by_name("theform").click()
        #wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
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
        wd.find_element_by_link_text("home").click()
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
        self.change_field("fax", contact.faxphone)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("byear", contact.byear)
        self.change_field("homepage", contact.homepage)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.secondaryphone)
        self.change_field("notes", contact.notes)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_contacts_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        if self.contact_cash is None:
            self.contact_cash = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                emails=cells[4].text
                phones=cells[5].text
                if len(cells[9].find_elements_by_tag_name("a")):
                    homepage = cells[9].find_element_by_tag_name("a").get_attribute("href")
                else:
                    homepage = None
                self.contact_cash.append(Contact(firstname=first_name, lastname=last_name, id=id, all_emails=emails, all_phones=phones,
                            address=address, homepage=homepage))
        return list(self.contact_cash)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell =row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell =row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        midname = wd.find_element_by_name("middlename").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        company= wd.find_element_by_name("company").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        byear= wd.find_element_by_name("byear").get_attribute("value")
        homepage= wd.find_element_by_name("homepage").get_attribute("value")
        address2= wd.find_element_by_name("address2").get_attribute("value")
        notes= wd.find_element_by_name("notes").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, midname=midname, nickname=nickname, address=address, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, title=title, company=company, email=email, email2=email2,
                       email3=email3, byear=byear, homepage=homepage,address2=address2,notes=notes)

    def get_contact_info_from_view_page(self, index):
        def find_phone(pattern, text):
            res = re.search(pattern, text)
            if res is not None:
                phone = res.group(1)
            else:
                phone = ""
            return phone

        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = find_phone("H:(.*)", text)
        mobilephone = find_phone("M:(.*)", text)
        workphone = find_phone("W:(.*)", text)
        secondaryphone = find_phone("P:(.*)", text)
        fullname= wd.find_element_by_id("content").find_element_by_tag_name("b").text
        emails = re.findall("(\w+@\w+(?:\.\w+)+)", text)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)
