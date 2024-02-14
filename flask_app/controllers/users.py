from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users import User
from flask import flash

#This is where the user can be routed and do CRUD
#The Links page

@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/create/new_user', methods=['POST'])
def save_user_info():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print(data)
    User.save_user(data)
    return redirect('/')