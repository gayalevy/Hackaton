import pyrebase
import Consts
import firebase_admin
from firebase_admin import credentials

# pip3 install pyrebase4


firebase = pyrebase.initialize_app(Consts.FIREBASE_CONFIG)
auth = firebase.auth()


def sign_up():
    print("sign up")
    email = input("enter email: ")
    password = input("enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("successfully registered")
    except:
        print("email already exist")


def log_in():
    print("sign in")
    email = input("enter email: ")
    password = input("enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("successfully logged in")
    except:
        print("email or password is incorrect")

db = firebase.database()

donation = {"donated": "yes", "amount": 70}

address = {"address": {"addres_4": donation,
                       "addres_3": donation
                       }}
pair = {"ofir and maria": address}

all_pairs = {"pairs": pair}
db.push(all_pairs)


db.child().child("pairs").child("ofir and maria").set(address)
