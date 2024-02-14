from flask_app.models.users import User
from flask_app.controllers import users
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)

#This should remians simple as this is our root for our application