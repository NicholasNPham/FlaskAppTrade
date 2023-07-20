from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)

# Database General Setup

db = SQLAlchemy()
DB_NAME = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)

class User(db.Model, UserMixin):
	
	# General Database Appending Method
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
	
	# Username
	username = StringField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Username'})
	
	# Password
	password = PasswordField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Password'})
	
	# Submit Button
	submit = SubmitField('Register')

	def validate_username(self, username):
		existing_user_username = User.query.filter_by(
			username = username.data).first()
		if existing_user_username:
			raise ValidationError("That Username Already Exists.")

class LoginForm(FlaskForm):
	
	# Username
	username = StringField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Username'})
	
	# Password
	password = PasswordField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Password'})
	
	# Submit Button
	submit = SubmitField('Login')

class AnalysisForm(FlaskForm):

	# Symbol
	symbol = StringField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Symbol'})
	
# Screener
	screener = StringField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Screener'})
	
	# Exchange
	exchange = StringField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Exchange'})
	
	# Interval
	interval = StringField(validators = [InputRequired(), Length(min = 4, max = 20)],
			render_kw = {'placeholder': 'Interval'})
	
	# Submit Button
	submit = SubmitField('Get Analysis')

# Routes

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():  
	form = RegisterForm()
	return render_template('register.html', form = form)

@app.route('/info')
def info():
	return render_template('info.html')

@app.route('/analysis', methods = ['GET', 'POST'])
def analysis():
	form = AnalysisForm()
	return render_template('analysis.html', form = form)

# Run Method

if __name__ == '__main__':
	app.run(debug=True)

