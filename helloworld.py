from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    return "This is the index page, nothing exciting here."


@app.route("/hello")
def hello_stranger():
    return "Hello, stranger! Try using /hello/<some_name> instead."


@app.route("/hello/<name>")
def hello_friend(name):
    return f"Hello, {name}!"


@app.route("/template/<name>")
def template(name=None):
    return render_template("firsttemplate.html", name=name)


@app.route("/color/<color>")
def color(color=None):
    return render_template("color.html", color=color)
