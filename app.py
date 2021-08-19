from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def initial_page():
    return "Hello World this is my first Flask application!"