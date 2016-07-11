from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app, 'login_and_registration')

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)