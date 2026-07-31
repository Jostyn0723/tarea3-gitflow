from flask import Flask
from database import init_db

app = Flask(__name__)
init_db()


@app.route("/")
def home():
    return "Task Manager - modelo de datos listo"


if __name__ == "__main__":
    app.run(debug=True)