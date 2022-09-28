from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.users import User


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_cooked = data["date_cooked"]
        self.under_cert_time = data["under_cert_time"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_id = data["users_id"]
        self.poster = None

    @staticmethod
    def validate(data):
        is_valid = True
        # TODO add validations here
        if len(data["name"]) < 3:
            flash(" Name Must be longer than 3 characters!")
            is_valid = False

    
        if len(data["description"]) < 3:
            flash(" Description Must be longer than 3 characters!")
            is_valid = False

        if len(data["instructions"]) < 3:
            flash(" Instructions Must be longer than 3 characters!")
            is_valid = False

        return is_valid
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id;"
        results = connectToMySQL("users_recipes").query_db(query)

        recipes = []

        for result in results:
            one_instance = cls(result)
            
            poster_data = {
                "id": result["users.id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "email": result["email"],
                "password": result["password"],
                "created_at": result["users.created_at"],
                "updated_at": result["users.updated_at"]
            }
            one_instance.poster = User(poster_data)
            recipes.append(one_instance)
        return recipes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, under_cert_time, created_at, updated_at, users_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_cert_time)s, NOW(), NOW(), %(users_id)s)"

        recipe_id = connectToMySQL("users_recipes").query_db(query, data)
        print(recipe_id)
        return recipe_id

    @classmethod
    def submit_edit(cls, data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_cooked=%(date_cooked)s,under_cert_time=%(under_cert_time)s,updated_at=NOW() WHERE id=%(id)s;"
        connectToMySQL("users_recipes").query_db(query, data)
        return True

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL("users_recipes").query_db(query, data)
        print(results)
        single_recipe = cls(results[0])
        return single_recipe

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL("users_recipes").query_db(query, data)
        
        
        
        
        
        

