from model.contact import Contact
import random
import string
import jsonpickle
import getopt
import sys
import os.path


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:p:", ["number of contacts", "file", "prefix"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

n = 5
f = "data/contacts.json"
p = ""

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
    elif o == "-p":
        p = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return p + prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


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
            for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
