
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
    # print(results)
    
    return all_users