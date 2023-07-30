
from pymysqlconnection import connectToMySQL

class User: 
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_cr").query_db(query)
        all_users = []
        for row in results:
            user = cls(row)
            all_users.append(user)
        return all_users

    @classmethod
    def create_user(cls,data_dict):

        query = """INSERT INTO users (first_name,last_name,email)
                    VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        
        result = connectToMySQL("users_cr").query_db(query,data_dict)
        
        return result

    @classmethod
    def show(cls, data_dict):

        query = """UPDATE users SET first_name  = %(first_name)s, last_name = %(last_name)s,
                    email= %(email)s;"""
        
        return connectToMySQL("users_cr").query_db(query, data_dict)

    
    @classmethod
    def get_one_by_id(cls,data_dict):

        query = """SELECT * FROM users WHERE id = %(id)s"""
        
        results = connectToMySQL("users_cr").query_db(query,data_dict)
        user  = cls(results[0])
        return user

    @classmethod
    def update_user(cls,data_dict):
        query = """UPDATE users 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s 
                WHERE id = %(id)s;"""
        return connectToMySQL('users_cr').query_db(query,data_dict)


    @classmethod
    def delete(cls,data_dict):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        result  = connectToMySQL('users_cr').query_db(query,data_dict)
        return None
    


