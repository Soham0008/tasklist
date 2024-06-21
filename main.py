from flask import Flask, render_template, request, redirect, url_for
from DB import getTaskList, addTask,updateTask,deleteTask
app = Flask(__name__)

# TaskList=[["learn backEnd",True],["frontend Task",False],["AI/ML",False]]

@app.route("/")
def home():
    TaskList= getTaskList()
    return render_template("tasklist.html", tasklist =TaskList)

@app.route("/add",methods=['POST'])
def add():
    taskname=request.form['taskName']
    duedate= request.form['dueDate']
    addTask(taskname,duedate)
    return redirect(url_for('home'))

@app.route("/update", methods=['POST'])
def update():
    updatedtaskname = request.form['updateTask']
    id = request.form['id']
    button = request.form['saveOrDelete']
    if button == "save":
        updateTask(updatedtaskname,id)
    elif button == "X":
        deleteTask(id)
    return redirect(url_for('home'))

app.run()