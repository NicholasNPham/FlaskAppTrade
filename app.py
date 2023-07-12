from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'

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

if __name__ == '__main__':
	app.run(debug=True)

