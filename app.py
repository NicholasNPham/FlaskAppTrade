from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

# Dababase General Setup

db = SQLAlchemy()
DB_NAME = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SECRET_KEY'] = 'secret'

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False)
	password = db.Column(db.String(80), nullable=False)

# Routes

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/info')
def info():
	return render_template('info.html')

@app.route('/analysis')
def analysis():
	return render_template('analysis.html')

# Run Method

if __name__ == '__main__':
	app.run(debug=True)

