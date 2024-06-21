from flask import Flask, render_template

app = Flask(__name__)

TaskList=[["backEnd",True],["frontend",False],["AI/ML",False]]
@app.route("/")
def hello_world():
    return render_template("tasklist.html", tasklist =TaskList)

app.run()