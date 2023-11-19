from db import db
from sqlalchemy import text


# just for testing
def get_motivation(user_id):
    sql = (
        "SELECT response, created_at FROM data WHERE question_id=1 AND user_id=:user_id"
    )
    return db.session.execute(text(sql), {"user_id": user_id}).fetchall()


def get_all_data(user_id):
    sql = """SELECT questions.question_text, data.response, data.created_at 
        FROM questions JOIN data ON questions.question_id=data.question_id WHERE data.user_id = :user_id;"""
    return db.session.execute(text(sql), {"user_id": user_id}).fetchall()
