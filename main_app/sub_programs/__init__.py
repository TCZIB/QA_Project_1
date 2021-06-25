from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("secretKey")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("databaseLogin")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

user = os.popen('whoami').read()


words = open(("/home/"+str(user[:-1])+"/QA_Project_1/main_app/sub_programs/static/blacklisted_words.txt"), 'r')
lines = words.readlines()

profanities = []

for line in lines:
    profanities.append(line[:-1])

accepted_ages = ["G","U","PG","PG-13","12","15","R","18","NC-17","R-18"]

from sub_programs import routes