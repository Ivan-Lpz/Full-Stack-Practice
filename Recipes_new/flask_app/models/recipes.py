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

        if len(data["date_cooked"]) == 0:
            flash("Must have cooked Date!")
            flash("ALL FIELDS REQUIRED")
            is_valid = False

        if len(data["name"]) == 0:
            flash("Must have Name!")
            flash("ALL FIELDS REQUIRED")
            is_valid = False
        
        if len(data["description"]) == 0:
            flash("Must have Description!")
            flash("ALL FIELDS REQUIRED")
            is_valid = False

        if len(data["instructions"]) == 0:
            flash("Must have Instructions!")
            flash("ALL FIELDS REQUIRED")
            is_valid = False


        return is_valid

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id;"
        results = connectToMySQL("recipes_new").query_db(query)

        recipes = []
        
        for row_from_db in results:
            one_recipe = cls(row_from_db)

            poster_data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            one_recipe.poster = User(poster_data)
            recipes.append(one_recipe)

        return recipes
    

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, under_cert_time, created_at, updated_at, users_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_cert_time)s, NOW(), NOW(), %(users_id)s)"

        recipe_id = connectToMySQL("recipes_new").query_db(query, data)
        print(recipe_id)
        return recipe_id


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL("recipes_new").query_db(query, data)
        print(results)
        single_recipe = cls(results[0])
        return single_recipe

    @classmethod
    def submit_edit(cls, data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_cooked=%(date_cooked)s,under_cert_time=%(under_cert_time)s,updated_at=NOW() WHERE id=%(id)s;"
        connectToMySQL("recipes_new").query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL("recipes_new").query_db(query, data)
        
        
        
        
        
        
        
        

    