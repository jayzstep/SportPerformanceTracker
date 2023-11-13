from app import app, db
from flask import render_template
from sqlalchemy import text


@app.route("/")
def home():
    result = db.session.execute(text("SELECT * FROM questions"))
    questions = result.fetchall()
    return render_template("index.html", questions=questions)


@app.route("/query")
def query():
    return render_template("query.html")
