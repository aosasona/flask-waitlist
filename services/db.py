from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv

load_dotenv('.env')


# Mongo URI
MONGO_URI = environ.get("MONGO_URI")

# Create connection to (local) database
client = MongoClient(MONGO_URI)

db = client.flaskify

col = db.waitlist


"""
Find an email
"""


def find_email(email):
    find_mail = col.find({"email": email.lower()})
    return len(list(find_mail))


"""
Insert new email
"""


def insert(email):
    add_user = col.insert_one({"email": email.lower()})
    if add_user.acknowledged is True:
        return True
    else:
        return False


"""
Find all users on the list
"""


def show():
    fetch_all = col.find()
    if fetch_all is not None:
        return fetch_all
    else:
        return False

