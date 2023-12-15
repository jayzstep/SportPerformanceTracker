import os
from db import db
from flask import session, abort, request
from sqlalchemy import text
import bcrypt


def login(username, password):
    result = db.session.execute(
        text("SELECT id, password, admin FROM users WHERE username=:username"),
        {"username": username},
    )

    user = result.fetchone()
    if not user:
        return False
    stored_password = user[1]
    if not stored_password:
        return False
    if not bcrypt.checkpw(password.encode(), stored_password.encode()):
        return False
    session["user_id"] = user[0]
    session["username"] = username
    session["csrf_token"] = os.urandom(16).hex()
    return True


def logout():
    del session["user_id"]
    del session["username"]
    del session["csrf_token"]


def add_new_user(username, password, role, full_name, sport, team):
    salt = bcrypt.gensalt()
    hash_value = bcrypt.hashpw(password.encode(), salt)
    try:
        db.session.execute(
            text(
                "INSERT INTO users (username, password, admin, full_name, sport, team) VALUES (:username, :password, :admin, :full_name, :sport, :team)"
            ),
            {
                "username": username,
                "password": hash_value.decode(),
                "admin": role,
                "full_name": full_name,
                "sport": sport,
                "team": team,
            },
        )

        db.session.commit()
        print("New user added successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return login(username, password)


def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
