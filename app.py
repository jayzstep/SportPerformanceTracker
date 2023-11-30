from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
import routes


# TODO confirm to user that data was saved successfully
# TODO questions to drop down menu
