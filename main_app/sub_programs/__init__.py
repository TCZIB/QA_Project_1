from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("secretKey")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("databaseLogin")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
user_path = parentDirectory + "/main_app/sub_programs/static/blacklisted_words.txt"

words = open(user_path, 'r')
lines = words.readlines()

profanities = []

for line in lines:
    profanities.append(line[:-1])

from sub_programs import routes