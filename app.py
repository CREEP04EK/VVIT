import requests
from flask import Flask, render_template, request
import psycopg2
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    host ='127.0.0.1',
    user ='root',
    password = 'qazwsxedc',
    port = '3306',
    database ='service_db'
)
cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/',methods=['POST'])
def logen():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service_db.`service.users` WHERE login=%s AND password=%s",(str(username),str(password)))
    records = list(cursor.fetchall())
    if len(records) == 0 and (len(username)>=1 or len(password) >=1) :
        return render_template('Not user in db.html'), print(records,password,username)
    elif len(records) == 0:
        return render_template('zero.html'),print(records,password,username)
    else:
        return render_template('account.html',full_name=records[0][1],login=records[0][2],password=records[0][3]),print(records,password,username)
