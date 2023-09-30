from flask import request, redirect
from werkzeug.security import generate_password_hash

from models import db, User
from admin import is_admin


def login_user():
    json_data = request.get_json()

    username = json_data.get('username')
    password = json_data.get('password')
    
    token = is_admin(username=username, password=password)

    if token:
        return token
    else:
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            errro_message = f'ERROR APPENDING USER IN DATABSE {e}'
            return errro_message, 401

    
