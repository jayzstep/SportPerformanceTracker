from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
import routes

# TODO check if user is logged in
# TODO confirm to user that data was saved successfully
# TODO check if user is admin
