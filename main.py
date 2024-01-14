import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_url_path="/static")

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
