from app import app
from db import db
from flask import render_template, request, redirect, session
from sqlalchemy import text
from flask import request
import users
import db_queries


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user_data")
def user_data():
    if "user_id" in session:
        user_data = db_queries.get_all_data(session["user_id"])
        if user_data:
            return render_template("user_data.html", user_data=user_data)
        else:
            return "No data found for this user", 404
    else:
        return "Unauthorized", 403


@app.route("/poll")
def poll():
    result = db.session.execute(text("SELECT * FROM questions"))
    questions = result.fetchall()
    return render_template("poll.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    users.check_csrf()

    form_data = {k: v for k, v in request.form.items() if k != "csrf_token"}

    for question_id, response_value in form_data.items():
        print(f"Question ID: {question_id}, Response Value: {response_value}")

        db.session.execute(
            text(
                "INSERT INTO Data (question_id, user_id, response) VALUES (:question_id, :user_id, :response)"
            ),
            {
                "question_id": question_id,
                "user_id": session["user_id"],
                "response": response_value,
            },
        )

    db.session.commit()
    print("Answers saved successfully!")
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
    users.add_new_user(username, password, False)
    return redirect("/")


@app.route("/register")
def register():
    return render_template("register.html")
