from db import db
from sqlalchemy import text


def get_poll():
    sql = "SELECT * FROM questions"
    return db.session.execute(text(sql)).fetchall()


# just for testing
def get_single_data(question_id, user_id):
    sql = "SELECT response, created_at FROM data WHERE question_id=:question_id AND user_id=:user_id"
    data = db.session.execute(
        text(sql), {"question_id": question_id, "user_id": user_id}
    ).fetchall()
    labels = [row[1].strftime("%Y-%m-%d") for row in data]
    values = [row[0] for row in data]
    print("labels:", labels)
    print("values:", values)
    return labels, values


def get_all_data(user_id):
    sql = """SELECT questions.question_text, data.response, data.created_at 
        FROM questions JOIN data ON questions.question_id=data.question_id WHERE data.user_id = :user_id;"""
    return db.session.execute(text(sql), {"user_id": user_id}).fetchall()


def add_data(question_id, user_id, response):
    db.session.execute(
        text(
            "INSERT INTO Data (question_id, user_id, response) VALUES (:question_id, :user_id, :response)"
        ),
        {
            "question_id": question_id,
            "user_id": user_id,
            "response": response,
        },
    )
    db.session.commit()
    print("Answers saved successfully!")
    return
