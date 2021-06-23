from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv{"secretKey"}
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv{"databaseLogin"}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

from sub_programs import routes