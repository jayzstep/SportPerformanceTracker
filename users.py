import os
from db import db
from flask import session, abort, request
from sqlalchemy import text
import bcrypt


def login(username, password):
    result = db.session.execute(
        text("SELECT password FROM users WHERE username=:username"),
        {"username": username},
    )

    user = result.fetchone()
    if not user:
        return False
    if not bcrypt.checkpw(password.encode(), user[0].encode()):
        return False
    session["username"] = username
    session[user_id] = user.id
    session[admin] = user.admin
    session["csrf_token"] = os.urandom(16).hex()
    return True


def logout():
    del session["username"]
    del session["user_id"]
    del session["admin"]


def add_new_user(username, password, role):
    salt = bcrypt.gensalt()
    hash_value = bcrypt.hashpw(password.encode(), salt)
    try:
        db.session.execute(
            text(
                "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"
            ),
            {"username": username, "password": hash_value, "admin": role},
        )

        db.session.commit()
        print("New user added successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return login(username, password)
