from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    
    ################# SAVE NEW NINJA #################
    @classmethod
    def save(cls, data):
        query = '''INSERT INTO dojos (name, created_at, updated_at)
            VALUES (%(name)s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());'''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
    
    ################# RETURN LIST OF NINJA #################
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in dojos_from_db
            dojos.append(cls(dojo))
        return dojos
    
    ################# RETURN SINGLE NINJA #################
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos WHERE dojos.id = %(id)s;'
        dojo_from_db = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(dojo_from_db[0])
    
    ################# UPDATE NINJA #################
    @classmethod
    def update(cls, data):
        query = '''UPDATE dojos SET 
                name = %(name)s,
                updated_at = CURRENT_TIMESTAMP()
                WHERE dojos.id = %(id)s;
                '''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    ################# DELETE NINJA #################
    @classmethod
    def delete_dojo(cls, data):
        query = 'DELETE FROM dojos WHERE dojos.id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    
        