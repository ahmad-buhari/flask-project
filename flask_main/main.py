from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def welcome():
    return render_template("welcome.html",
    message = "Here's a message from the view, its so cool!"
    )

@app.route("/report")
def report():
    return render_template("welcome.html", message = "New report page blabla" , sub = "New Category")