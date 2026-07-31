from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from database import init_db, insert_task, get_all_tasks, get_task, update_task, delete_task

app = Flask(__name__)
init_db()


@app.template_filter("fecha_bonita")
def fecha_bonita(value):
    """Convierte una fecha YYYY-MM-DD a formato DD/MM/AAAA para mostrarla al usuario."""
    if not value:
        return ""
    try:
        return datetime.strptime(value, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        return value


@app.route("/")
def home():
    tasks = get_all_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description", "")
        due_date = request.form.get("due_date", "")
        insert_task(title, description, due_date)
        return redirect(url_for("home"))
    return render_template("create.html")


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = get_task(task_id)
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description", "")
        due_date = request.form.get("due_date", "")
        status = request.form.get("status", "pendiente")
        update_task(task_id, title, description, due_date, status)
        return redirect(url_for("home"))
    return render_template("edit.html", task=task)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)