from app import app, db
from flask import render_template
from sqlalchemy import text
from flask import request


@app.route("/")
def home():
    result = db.session.execute(text("SELECT * FROM questions"))
    questions = result.fetchall()
    return render_template("index.html", questions=questions)


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
