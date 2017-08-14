import pymysql.cursors
#import mysql.connector
from model.group import Group
from model.contact import Contact

class DBFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
#        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection = pymysql.connect(host=host, database=name,user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        self.connection.commit()
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where deprecated = 0")
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                list.append(Group(gr_id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        self.connection.commit()
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, " +
                           "work, fax, email, email2, email3, byear, homepage, address2, phone2, notes from addressbook where deprecated = 0")
            for row in cursor.fetchall():
                (id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email, email2, email3,
                                byear, homepage, address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, midname=middlename, lastname=lastname, nickname=nickname,
                                      title=title, company=company, address=address, homephone=home, mobilephone=mobile,
                                      workphone=work, fax=fax, email=email, email2=email2, email3=email3, byear=byear,
                                      homepage=homepage, address2=address2, secondaryphone=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

