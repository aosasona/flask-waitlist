from pymongo import MongoClient

# Create connection to local database
con = MongoClient("localhost", 27017)

db = con.flaskify

col = db.waitlist

"""
Insert new email
"""


def insert(email):
    find_mail = col.find_one({"email": email.lower()})

    if find_mail is None:
        col.insert_one({"email": email.lower()})
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
