from db import db
from sqlalchemy import text
from datetime import date


# poll


def get_poll():
    sql = "SELECT * FROM questions"
    return db.session.execute(text(sql)).fetchall()


# get user data


def get_single_data(question_id, user_id):
    sql = "SELECT response, created_at FROM data WHERE question_id=:question_id AND user_id=:user_id"
    data = db.session.execute(
        text(sql), {"question_id": question_id, "user_id": user_id}
    ).fetchall()
    labels = [{"date": row[1].strftime("%Y-%m-%d"), "value": row[0]} for row in data]
    print("labels:", labels)
    return labels


def get_menstrual_data(user_id):
    sql = """
        SELECT data.response, data.created_at
        FROM data
        JOIN users ON data.user_id = users.id
        JOIN questions ON data.question_id = questions.question_id
        WHERE questions.question_title = 'Menstrual cycle day 1' AND users.id=:user_id;
    """
    data = db.session.execute(text(sql), {"user_id": user_id}).fetchall()
    labels = [{"date": row[1].strftime("%Y-%m-%d"), "value": row[0]} for row in data]
    print("labels:", labels)
    return labels


def get_question_title(question_id):
    sql = "SELECT question_title FROM questions WHERE question_id=:question_id"
    return db.session.execute(text(sql), {"question_id": question_id}).fetchone()[0]


def get_radio_scale(question_id):
    sql = "SELECT radio_scale FROM questions WHERE question_id=:question_id"
    return db.session.execute(text(sql), {"question_id": question_id}).fetchone()[0]


def get_questions_for_menu():
    sql = "SELECT question_id, question_title, radio_scale FROM questions WHERE radio_scale >= 5"
    return db.session.execute(text(sql)).fetchall()


def get_all_data(user_id):
    sql = """SELECT questions.question_text, data.response, data.created_at 
        FROM questions JOIN data ON questions.question_id=data.question_id WHERE data.user_id = :user_id;"""
    return db.session.execute(text(sql), {"user_id": user_id}).fetchall()


# add data


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
    today = date.today()
    db.session.execute(
        text("UPDATE users SET poll_updated_at = :today WHERE id = :user_id"),
        {"today": today, "user_id": user_id},
    )
    db.session.commit()
    return


# checks


def check_poll_updated(user_id):
    sql = "SELECT poll_updated_at FROM users WHERE id=:user_id"
    date_updated = db.session.execute(text(sql), {"user_id": user_id}).fetchone()[0]
    if date_updated == date.today():
        return True
    else:
        return False
