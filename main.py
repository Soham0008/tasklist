from flask import Flask, render_template

app = Flask(__name__)

TaskList=[["learn backEnd",True],["frontend Task",False],["AI/ML",False]]
@app.route("/")
def hello_world():
    return render_template("tasklist.html", tasklist =TaskList)

app.run()