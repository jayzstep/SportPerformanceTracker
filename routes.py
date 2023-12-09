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
    category_averages = poll_helper.get_category_averages(1)
    tips = poll_helper.get_usertips(session["user_id"])
    return render_template("testi.html", averages=category_averages, tips=tips)


@app.route("/")
def index():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("index.html")


@app.route("/user_data", methods=["POST", "GET"])
def user_data():
    if "user_id" not in session:
        return redirect("/")

    title = ""
    radio_scale = 1
    chart_data = []
    menstrual_data = []
    questions = poll_helper.get_questions_for_menu()
    tips = [tip[0] for tip in poll_helper.get_usertips(session["user_id"])]

    if request.method == "POST":
        question_id = request.form["question_id"]
        chart_data = poll_helper.get_single_data(question_id, session["user_id"])
        menstrual_data = poll_helper.get_menstrual_data(session["user_id"])
        title = poll_helper.get_question_title(question_id)
        radio_scale = poll_helper.get_radio_scale(question_id)
        if not chart_data:
            return "No data found", 404  #! change to error page?

    return render_template(
        "user_data.html",
        chart_data=chart_data,
        menstrual_data=menstrual_data,
        title=title,
        questions=questions,
        radio_scale=radio_scale,
        tips=tips,
    )


@app.route("/poll")
def poll():
    if "user_id" not in session:
        return redirect("/")
    if poll_helper.check_poll_updated(session["user_id"]):
        return render_template(
            "/error.html", message="You have already answered the poll today"
        )
    questions = poll_helper.get_poll()
    return render_template("poll.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    users.check_csrf()

    form_data = {k: v for k, v in request.form.items() if k != "csrf_token"}

    for question_id, response_value in form_data.items():
        poll_helper.add_data(question_id, session["user_id"], response_value)

    averages = poll_helper.get_category_averages(session["user_id"])

    for category, average in averages:
        if not category:
            continue
        if average < 3:
            poll_helper.add_usertip(session["user_id"], category)
    return redirect("/")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="Wrong credentials")
        session["username"] = username
        return redirect("/")
    return render_template("login.html")


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
