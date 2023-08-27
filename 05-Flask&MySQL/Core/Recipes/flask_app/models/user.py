from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask_app import DATABASE

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

#----------- CONSTRUCTOR ------------

class User():

    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict ['last_name']
        self.email = data_dict ['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.recipes_list = []


#---------- CRUD QUERIES -------------

# ******** Create a user *********  

    @classmethod
    def create_user(cls,data_dict):
        query = """INSERT INTO users (first_name,last_name,email,password) 
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s),;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
        
    # this method will return the id of the created user

# ******** Get all users **********  

    @classmethod
    def get_users(cls):
        query="SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        #organize the results
        users=[]
        for row in results:
            users.append(cls(row))
        return users
    
# ******* Get one user by id ******** 

    @classmethod
    def get_by_id(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result)<1:
            return False
        return cls(result[0])
    
# ****** Get one user by email ****** 

    @classmethod
    def get_by_email(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])

# ******** Validate a user ********  

    @staticmethod
    def validate_user(data):
            is_valid = True

            if len(data['first_name'])<2:
                flash("First Name must be more than 2 characters!","register")
                is_valid = False
            if len(data['last_name'])<2:
                flash("Last Name must be more than 2 characters!","register")
                is_valid = False
            if not EMAIL_REGEX.match(data['email']): 
                flash("Email must be valid !","register")
                is_valid = False
            elif User.get_by_email({'email':data['email']}):
                flash("Email already exist !","register")
                is_valid = False
            if len(data['password'])<8:
                flash("Password must be more than 8 characters!","register")
                is_valid = False
            elif data['password']!=data['confirm_password']:
                flash("Passwords do not match!","register")
                is_valid = False

            return is_valid


# @staticmethod
#     def validate_register(data_dict):
#         is_valid = True
#         if len(data_dict['first_name'])< 2:
#             print("First Name too short .....")
#             flash("First Name too short .....", "register")
#             is_valid = False
#         if len(data_dict['last_name'])< 2:
#             print("Last Name too short .....")
#             flash("Last Name too short .....", "register")
#             is_valid = False
#         if len(data_dict['password'])< 7:
#             print("Password too short .....")
#             flash("Password too short .....", "register")
#             is_valid = False
#         elif data_dict['password'] != data_dict['confirm_password']:
#             print("Password and Confirm password Don't match !!!!!")
#             flash("Password and Confirm password Don't match !!!!!", "register")
#             is_valid = False
#         if not EMAIL_REGEX.match(data_dict['email']): 
#             flash("Invalid email address!")
#             is_valid = False
#         elif User.get_by_email({'email':data_dict['email']}):
#             flash("Email Already taken . Hope by you !!!! ", "register")
#             is_valid = False
#         return is_valid
