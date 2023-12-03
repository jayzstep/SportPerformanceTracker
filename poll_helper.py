from db import db
from sqlalchemy import text
from datetime import date
from decimal import Decimal  #! remove


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
    return labels


def get_menstrual_data(user_id):
    sql = """
        SELECT data.response, data.created_at
        FROM data
        JOIN questions ON data.question_id = questions.question_id
        WHERE questions.question_title = 'Menstrual cycle day 1' AND data.user_id=:user_id AND data.response = 2;
    """

    data = db.session.execute(text(sql), {"user_id": user_id}).fetchall()
    labels = [{"date": row[1].strftime("%Y-%m-%d"), "value": row[0]} for row in data]
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


# testing new stuff


def get_sleep_average(user_id):
    sql = "SELECT ROUND(AVG(response), 1) FROM data WHERE user_id=:user_id AND question_id=4"
    return db.session.execute(text(sql), {"user_id": user_id}).fetchone()[0]


def get_category_averages(user_id):
    sql = """
        SELECT questions.category, ROUND(AVG(response), 1) 
        FROM data 
        JOIN questions ON data.question_id = questions.question_id 
        WHERE data.user_id=:user_id 
        GROUP BY questions.category"""
    result = db.session.execute(text(sql), {"user_id": user_id}).fetchall()

    averages = [(category, float(avg)) for category, avg in result]

    return averages


def get_tip_ids(category):
    sql = "SELECT tip_id FROM tips WHERE category=:category"
    return db.session.execute(text(sql), {"category": category}).fetchall()


def add_usertip(user_id, tip_id):
    try:
        db.session.execute(
            text("INSERT INTO usertips (user_id, tip_id) VALUES (:user_id, :tip_id)"),
            {
                "user_id": user_id,
                "tip_id": tip_id,
            },
        )
        db.session.commit()
    except:
        print("Usertip already exists")
    return


def get_usertips(user_id):
    sql = "SELECT tip_text FROM tips JOIN usertips ON tips.tip_id = usertips.tip_id WHERE usertips.user_id=:user_id"
    return db.session.execute(text(sql), {"user_id": user_id}).fetchall()


def get_all_tips():
    sql = "SELECT tip_text FROM tips"
    return db.session.execute(text(sql)).fetchall()


def add_mock_data(user_id):
    sql = """INSERT INTO Data (user_id, question_id, response, created_at)
VALUES 
  (:user_id, 1, 3, '2023-11-15 12:00:00'),
  (:user_id, 2, 2, '2023-11-15 12:00:00'),
  (:user_id, 3, 3, '2023-11-15 12:00:00'),
  (:user_id, 4, 4, '2023-11-15 12:00:00'),
  (:user_id, 5, 5, '2023-11-15 12:00:00'),
  (:user_id, 6, 4, '2023-11-15 12:00:00'),
  (:user_id, 7, 5, '2023-11-15 12:00:00'),
  (:user_id, 8, 6, '2023-11-15 12:00:00'),
  (:user_id, 9, 1, '2023-11-15 12:00:00'),
  (:user_id, 10, 1,'2023-11-15 12:00:00'),
  (:user_id, 1, 2, '2023-11-16 12:00:00'),
  (:user_id, 2, 3, '2023-11-16 12:00:00'),
  (:user_id, 3, 2, '2023-11-16 12:00:00'),
  (:user_id, 4, 4, '2023-11-16 12:00:00'),
  (:user_id, 5, 5, '2023-11-16 12:00:00'),
  (:user_id, 6, 5, '2023-11-16 12:00:00'),
  (:user_id, 7, 4, '2023-11-16 12:00:00'),
  (:user_id, 8, 8, '2023-11-16 12:00:00'),
  (:user_id, 9, 1, '2023-11-16 12:00:00'),
  (:user_id, 10, 1,'2023-11-16 12:00:00'),
  (:user_id, 1, 4, '2023-11-17 12:00:00'),
  (:user_id, 2, 4, '2023-11-17 12:00:00'),
  (:user_id, 3, 4, '2023-11-17 12:00:00'),
  (:user_id, 4, 5, '2023-11-17 12:00:00'),
  (:user_id, 5, 3, '2023-11-17 12:00:00'),
  (:user_id, 6, 2, '2023-11-17 12:00:00'),
  (:user_id, 7, 3, '2023-11-17 12:00:00'),
  (:user_id, 8, 2, '2023-11-17 12:00:00'),
  (:user_id, 9, 1, '2023-11-17 12:00:00'),
  (:user_id, 10, 2,'2023-11-17 12:00:00'),
  (:user_id, 1, 5, '2023-11-19 12:00:00'),
  (:user_id, 2, 2, '2023-11-19 12:00:00'),
  (:user_id, 3, 1, '2023-11-19 12:00:00'),
  (:user_id, 4, 2, '2023-11-19 12:00:00'),
  (:user_id, 5, 3, '2023-11-19 12:00:00'),
  (:user_id, 6, 4, '2023-11-19 12:00:00'),
  (:user_id, 7, 4, '2023-11-19 12:00:00'),
  (:user_id, 8, 6, '2023-11-19 12:00:00'),
  (:user_id, 9, 1, '2023-11-19 12:00:00'),
  (:user_id, 10, 1,'2023-11-19 12:00:00'),
  (:user_id, 1, 2, '2023-11-23 12:00:00'),
  (:user_id, 2, 3, '2023-11-23 12:00:00'),
  (:user_id, 3, 2, '2023-11-23 12:00:00'),
  (:user_id, 4, 4, '2023-11-23 12:00:00'),
  (:user_id, 5, 5, '2023-11-23 12:00:00'),
  (:user_id, 6, 5, '2023-11-23 12:00:00'),
  (:user_id, 7, 4, '2023-11-23 12:00:00'),
  (:user_id, 8, 8, '2023-11-23 12:00:00'),
  (:user_id, 9, 1, '2023-11-23 12:00:00'),
  (:user_id, 10, 1,'2023-11-23 12:00:00'),
  (:user_id, 1, 4, '2023-12-01 12:00:00'),
  (:user_id, 2, 4, '2023-12-01 12:00:00'),
  (:user_id, 3, 4, '2023-12-01 12:00:00'),
  (:user_id, 4, 5, '2023-12-01 12:00:00'),
  (:user_id, 5, 3, '2023-12-01 12:00:00'),
  (:user_id, 6, 2, '2023-12-01 12:00:00'),
  (:user_id, 7, 3, '2023-12-01 12:00:00'),
  (:user_id, 8, 2, '2023-12-01 12:00:00'),
  (:user_id, 9, 1, '2023-12-01 12:00:00'),
  (:user_id, 10, 2,'2023-12-01 12:00:00');
"""
    db.session.execute(text(sql), {"user_id": user_id})
    db.session.commit()
    return
