from pymongo import MongoClient
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from application import login
# #initialize database
client = MongoClient('localhost', 27017)
db = client['iot']

# @login.user_loader
# def load_user(id):
#     return db.users.find({"username": username})

class User():
    def __init__(self):
        self.is_authenticated = False
        self.username = ""
        self.password = ""

    def check_authentication(self):
        return self.is_authenticated
    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    def check_password(self, username, password):
        user_info = db.users.find({"username": username})
        if check_password_hash(user_info[0]['password'], password):
            self.username = username
            self.password = user_info[0]['password']
            self.is_authenticated = True
            return True
        else:
            return False

    # @classmethod
    # def check_credentials(self, un, pw):
