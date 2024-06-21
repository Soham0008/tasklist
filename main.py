from flask import Flask, render_template
from DB import getTaskList
app = Flask(__name__)

# TaskList=[["learn backEnd",True],["frontend Task",False],["AI/ML",False]]
TaskList= getTaskList()
@app.route("/")
def hello_world():
    return render_template("tasklist.html", tasklist =TaskList)

app.run()