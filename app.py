from flask import Flask, render_template, request, redirect, url_for
from database import init_db, insert_task

app = Flask(__name__)
init_db()


@app.route("/")
def home():
    return "Task Manager - modelo de datos listo"


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description", "")
        due_date = request.form.get("due_date", "")
        insert_task(title, description, due_date)
        return redirect(url_for("home"))
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)