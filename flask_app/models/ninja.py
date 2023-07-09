from flask_app.config.mysqlconnection import connectToMySQL

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
        query = '''INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), %(dojo_id)s);'''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
    
    ################# RETURN LIST OF NINJA #################
    @classmethod
    def get_all(cls, data):
        query = 'SELECT * FROM ninjas;'
        ninjas_from_db = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        ninjas = []
        for ninja in ninjas_from_db:
            ninjas.append(cls(ninja))
        return ninjas
    
    ################# RETURN SINGLE NINJA #################
    @classmethod
    def get_one(cls, ninja_id):
        query = 'SELECT * FROM ninjas WHERE ninjas.id = %(id)s;'
        ninja_from_db = connectToMySQL('dojos_and_ninjas').query_db(query, {'id': ninja_id})
        return cls(ninja_from_db[0])
    
    ################# UPDATE NINJA #################
    @classmethod
    def update(cls, data):
        query = '''UPDATE ninjas SET 
                first_name = %(first_name)s,
                last_name = %(last_name)s,
                age = %(age)s,
                dojo_id = %(dojo_id)s,
                updated_at = CURRENT_TIMESTAMP()
                WHERE ninjas.id = %(id)s;
                '''
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    ################# DELETE NINJA #################
    @classmethod
    def delete_ninja(cls, ninja_id):
        query = 'DELETE FROM ninjas WHERE ninjas.id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas').query_db(query, {'id': ninja_id})

