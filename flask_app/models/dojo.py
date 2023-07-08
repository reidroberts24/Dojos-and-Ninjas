from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    ################# UPDATE NINJAS (instance method) #################
    def get_ninjas(self, data):
        query = '''SELECT * FROM ninjas
                WHERE ninjas.dojo_id = %(id)s;
                '''
        ninjas_from_db = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        for ninja_data in ninjas_from_db:
            ninja = Ninja(ninja_data)
            self.ninjas.append(ninja)
        return self.ninjas


    ################# SAVE NEW DOJO #################
    @classmethod
    def save(cls, data):
        query = '''INSERT INTO dojos (name, created_at, updated_at)
            VALUES (%(name)s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());'''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
    
    ################# RETURN LIST OF DOJOS #################
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos
    
    ################# RETURN SINGLE DOJO #################
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos WHERE dojos.id = %(id)s;'
        dojo_from_db = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(dojo_from_db[0])
    
    ################# UPDATE DOJO #################
    @classmethod
    def update(cls, data):
        query = '''UPDATE dojos SET 
                name = %(name)s,
                updated_at = CURRENT_TIMESTAMP()
                WHERE dojos.id = %(id)s;
                '''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    ################# DELETE DOJO #################
    @classmethod
    def delete_dojo(cls, data):
        query = 'DELETE FROM dojos WHERE dojos.id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    
        