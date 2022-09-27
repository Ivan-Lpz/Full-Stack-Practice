from flask_app.config.mysqlconnection import connectToMySQL
#here we are importing our flask app. config. my sqlconnection so that we can run our queries into our database
#each table should have its own model, f.e. in the dojos and ninjas assignment there are two table so you should have
#two models, one for each table. And these models are for querying each table
#the models is where we make interactions with our database 

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)

        users = []
        for result in results:
            one_instance = cls(result)
            users.append(one_instance)
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW(), NOW());"
        users_id = connectToMySQL("users_schema").query_db(query,data)
        return users_id

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"    # the * means that we are selecting every column not the rows. Also this line is how we can get one thing from the database

        results = connectToMySQL("users_schema").query_db(query,data)
        # print(results)
        single_user = cls(results[0])
        return single_user

    @classmethod
    def submit_edit(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id=%(id)s;"

        connectToMySQL("users_schema").query_db(query,data)
        return True

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)