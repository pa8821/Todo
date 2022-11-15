from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("tasks.db", check_same_thread=False)
connection.execute('''CREATE TABLE IF NOT EXISTS tasks (id integer PRIMARY KEY,task text);''')
cur = connection.cursor

@app.route('/', methods = ["GET", "POST"])
def index():
    if(request.method=="POST"):

        task = request.form.get("task")
        if(task):
            connection.execute("INSERT INTO tasks (task) VALUES (?)", [task])
            connection.commit()

        delete = request.form.get("tick")
        if(delete):
            connection.execute("DELETE FROM tasks WHERE id = ?", [delete])
            connection.commit()

        return redirect("./")
    else:
        cursor = connection.execute("SELECT * FROM tasks;")
        table = cursor.fetchall()
        return render_template("index.html", tasks = table)