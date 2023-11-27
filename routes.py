from app import app
from db import db
from flask import render_template, request, redirect, session
from sqlalchemy import text
from flask import request
import users
import poll_helper


@app.route("/testi")
def testi():
    if "user_id" not in session:
        return redirect("/")
    labels, values = poll_helper.get_motivation(session["user_id"])
    if user_data:
        return render_template("testi.html", labels=labels, values=values)
    else:
        return "No data found for this user", 404


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user_data")
def user_data():
    if "user_id" not in session:
        return redirect("/")
    user_data = poll_helper.get_all_data(session["user_id"])
    if user_data:
        return render_template("user_data.html", user_data=user_data)
    else:
        return "No data found for this user", 404


@app.route("/poll")
def poll():
    if "user_id" not in session:
        return redirect("/")
    questions = poll_helper.get_poll()
    return render_template("poll.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    users.check_csrf()

    form_data = {k: v for k, v in request.form.items() if k != "csrf_token"}

    for question_id, response_value in form_data.items():
        poll_helper.add_data(question_id, session["user_id"], response_value)
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if not users.login(username, password):
        return render_template("error.html", message="Wrong credentials")
    session["username"] = username
    return redirect("/")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/new_user", methods=["POST"])
def new_user():
    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["confirm_password"]
    if password != password2:
        return render_template("error.html", message="Passwords do not match")
    users.add_new_user(username, password, False)
    return redirect("/")


@app.route("/register")
def register():
    return render_template("register.html")
