from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, midname=None, lastname=None, nickname=None, title=None, company=None, street=None, homephone=None,
                       mobilephone=None, workphone=None, email=None, email2=None, byear=None, homepage=None, address2=None, notes=None):

        self.id = id
        self.firstname = firstname
        self.midname = midname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.street = street
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.email2 = email2
        self.byear = byear
        self.homepage = homepage
        self.address2 = address2
        self.notes = notes

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize