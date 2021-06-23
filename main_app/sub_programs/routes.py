from sub_programs import app, db
from flask import render_template, request, url_for

@app.route("/")
@app.route("/home")

def home_page():
    return "Welcome Home"