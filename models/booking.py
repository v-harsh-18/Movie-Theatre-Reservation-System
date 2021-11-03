from flask import *
from flask.sessions import SessionMixin
from flask_mysqldb import MySQL
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import os
import requests
import pathlib
from werkzeug.utils import secure_filename, send_file
import models.display as display
import models.booking as bookin
from flask_mail import *
import datetime

app=Flask(__name__)
app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5792'
app.config['MYSQL_DB'] = 'faculty_assignment'
app.config['UPLOAD_FOLDER'] = 'static/files'

app.secret_key = 'your secret key'
 
mysql = MySQL(app)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'notifyindia2021@gmail.com',
    MAIL_PASSWORD=  'bleh_bleh'
)
mail = Mail(app)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return redirect('/login')
        else:
            return function()

    return wrapper


def booking():
    login_is_required

    idshowing='Mimi0001121110513'
    title='Mimi'

    query='''
    SELECT seat 
    FROM reservation.seats
    WHERE idshowing=%s
    '''

    booked=[]

    cursor = mysql.connection.cursor()
    cursor.execute(query,[idshowing])
    seats=cursor.fetchall()
    cursor.close()

    for seat in seats:
        booked.append(seat[0])


    print(booked)
    return render_template('booking.html',seats=booked,title=title,idshowing=idshowing)   

def booked():
    if request.method=='POST':
     seats=request.form.getlist('book')

     booked=[]

     time=datetime.datetime.now()

     price=request.form['price']

     idshowing=request.form['idshowing']

     num=len(seats)

     selected=''

     for seat in seats:
         if seat!='':
          booked.append(seat)
          selected=selected+' '+seat

     query='''
    SELECT *
    FROM reservation.user_account
    WHERE user_id=%s'''

     status='''
    SELECT *
    FROM reservation.showing
    WHERE idShowing=%s'''

     user_id=session['google_id']

     cursor = mysql.connection.cursor()
     cursor.execute(query,[user_id])
     uid=cursor.fetchone()
     cursor.close()  

     cursor = mysql.connection.cursor()
     cursor.execute(status,[idshowing])
     status=cursor.fetchone()
     cursor.close()  
     

     print(seats)

    # mail.send_message('New message from ' + 'Cine Show', sender='Cine Show', recipients = [uid[1]], body = 'message' + "\n" + 'phone')    
    
     return redirect('/confirmation')