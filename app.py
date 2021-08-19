import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template

# settings 
DATABASE = 'blog.db'
SECRET_KEY = 'flan'

app = Flask(__name__)
app.config.from_object(__name__)

def db_connect():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_req():
    g.db = db_connect()

@app.teardown_request
def after_req(exc):
    g.db.close()

@app.route('/')
def display_posts():
    return render_template('display_posts.html')

@app.route("/hello")
def hello_page():
    return "Hello World this is my first Flask application!"
