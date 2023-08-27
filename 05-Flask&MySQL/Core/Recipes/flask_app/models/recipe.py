from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app import DATABASE

#----------- CONSTRUCTOR ------------

class Recipe():
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30min = data['under_30min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.poster = user.User.get_by_id({'id':self.user_id})


#---------- CRUD QUERIES -------------

#******** Create a recipe *********

    @classmethod
    def create_recipe(cls,data):
        query = """INSERT INTO recipes (user_id,name,description,instructions,date_cooked,under_30min) 
                    VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s,
                            %(date_cooked)s,%(under_30min)s);"""

        return connectToMySQL(DATABASE).query_db(query,data)

        # this query will return the id of the new recipe insert
        
#******** Get all recipes *********  
    @classmethod
    def get_cars(cls):
        query="SELECT * FROM recipes;"

        results= connectToMySQL(DATABASE).query_db(query)
        #organize the results
        recipes = []
        for row in results:
            recipess.append(cls(row))
        return recipes
    
#******** Get one by id *********   

    @classmethod
    def get_by_id_recipe(cls,data):
        query="SELECT * FROM recipes WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

#******** Update recipe **********  
    
    @classmethod
    def update_recipe(cls,data):
        query = """UPDATE recipes SET 
                    name=%(name)s,description=%(description)s,instructions=%(instructions)s,
                    date_cooked=%(date_cooked)s ,under_30min=%(under_30min)s
                    WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)

#********* Delete recipe **********  
    
    @classmethod
    def delete_recipe(cls,data):
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

#********* Validate recipe **********  

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name'])<3:
            flash("Name must be more than 3 characters", "recipe")
            is_valid =False
        if len(data['description'])<3:
            flash("Description lust not be blank ", "recipe")
            is_valid =False
        if len(data['instructions']) <3:
            flash("instructions must be more than 3 ", "recipe")
            is_valid = False
        if data['made_date'] == "":
            flash("Made Date must not blank", "recipe")
            is_valid = False
        return is_valid




