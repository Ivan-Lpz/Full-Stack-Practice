from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        
        dojos = []
        for result in results:
            one_instance = cls(result)
            dojos.append(one_instance)
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

        one_dojo = cls(results[0])
        return one_dojo

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)


