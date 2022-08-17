from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum
import os


# Configuration
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Required Database Models






@app.route('/')
def get_todos():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)