from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# This is where our queries are made for MYSQL

class User:
    DB = 'email_validation_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def save_user(cls,data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s)
                """
        print(query)
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @staticmethod
    def validate_users_info(cls):
        is_valid = True
        if len(cls['first_name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(cls['last_name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(cls['email']) < 3:
            flash("Email is required.")
            is_valid = False
        pass
    #Need to check with email has the required special chracters in the check.
