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


def booki():
    if request.method=='POST':
     seats=request.form.getlist('book')
     booked=[]

     for seat in seats:
         if seat!='':
          booked.append(seat)

     query='''
    SELECT *
    FROM reservation.user_account
    WHERE user_id=%s'''

     user_id=session['google_id']

     cursor = mysql.connection.cursor()
     cursor.execute(query,[user_id])
     uid=cursor.fetchone()
     cursor.close()  

     print(uid[1])
   

     mail.send_message('New message from ' + 'Cine Show', sender='Cine Show', recipients = [uid[1]], body = 'message' + "\n" + 'phone')    
    
     return redirect('/confirmation')