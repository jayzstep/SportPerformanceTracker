from app import app
from db import db
from flask import render_template, request, redirect, session
from sqlalchemy import text
from flask import request
import users


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/poll")
def home():
    result = db.session.execute(text("SELECT * FROM questions"))
    questions = result.fetchall()
    return render_template("poll.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    for question_id in request.form:
        response_value = request.form[question_id]
        print(f"Question ID: {question_id}, Response Value: {response_value}")

        db.session.execute(
            text(
                "INSERT INTO Data (question_id, response) VALUES (:question_id, :response)"
            ),
            {"question_id": question_id, "response": response_value},
        )

    db.session.commit()

    return "Answers saved successfully!"


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if not users.login(username, password):
        return render_template("error.html", message="Wrong credentials")
    session["username"] = username
    return redirect("/")


@app.route("/logout", methods=["POST"])
def logout():
    logout()
    return redirect("/")


@app.route("/new_user", methods=["POST"])
def new_user():
    username = request.form["username"]
    password = request.form["password"]
    users.add_new_user(username, password, False)
    return redirect("/")


@app.route("/register")
def register():
    return render_template("register.html")
