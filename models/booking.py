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
from flask_mail import *
import datetime
import math

app=Flask(__name__)
app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5792'
app.config['MYSQL_DB'] = 'reservation'
app.config['UPLOAD_FOLDER'] = 'static/files'

app.secret_key = 'your secret key'
 
mysql = MySQL(app)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'cineshow.india@gmail.com',
    MAIL_PASSWORD=  '!Cineshow1'
)
mail = Mail(app)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return redirect('/login')
        else:
            return function()

    return wrapper

def timings():

    if "google_id" not in session:
            return redirect('/login')

    if request.method=='POST':
        title=request.form['title']
        date=request.form['date']
        print(date)

        query='''
        SELECT reservation.showing.idShowing, reservation.theatre_complex.name, reservation.theatre_complex.address, reservation.theatre_complex.phone_number,reservation.showing.start_time,showing.date_played,reservation.showing.theatre_id,reservation.showing.Theatre_screen_id
        FROM reservation.showing
        JOIN reservation.theatre_complex
        ON reservation.showing.theatre_id=reservation.theatre_complex.theatre_id
        WHERE reservation.showing.Movie_Title=%s AND reservation.showing.date_played=%s
        ORDER BY reservation.theatre_complex.theatre_id;
        '''

        cursor = mysql.connection.cursor()
        cursor.execute(query,[title,date])
        input=cursor.fetchall()
        cursor.close()

        theatre=()
        temp1=()
        temp2={}
        tval=0
        length=len(input)

        for i in range(0,length):
         if(i==0):
          temp1=(input[i][1],input[i][2],input[i][3],input[i][6],input[i][7])
          temp2[input[i][0]]=input[i][4]

         elif(input[i][1]==temp1[0]):
            temp2[input[i][0]]=input[i][4]

         else:
             if(tval==0):
              temp1+=(temp2,)
              theatre+=(temp1,)
              tval=1


             else: 
              temp1+=(temp2,)
              list1=list(theatre)
              list1.append(temp1)
              theatre=tuple(list1)

             temp1=(input[i][1],input[i][2],input[i][3],input[i][6],input[i][7])
             print(temp1)
             temp2={input[i][0]:input[i][4]}


        temp1+=(temp2,)
        list1=list(theatre)
        list1.append(temp1)
        theatre=tuple(list1)

        print(theatre)   
        return render_template('list.html',theatre=theatre, title=title)   

  

    return render_template('list.html')    


def booking():
    if "google_id" not in session:
            return redirect('/login')

    idshowing=request.form['idshowing']
    print(idshowing)
    title=request.form['title']

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

    if "google_id" not in session:
            return redirect('/login')

    if request.method=='POST':
     seats=request.form.getlist('book')

     booked=[]

     btime=datetime.datetime.now()
     btime=btime.timestamp()
     btime=btime*1000000
     btime=math.ceil(btime)
     btime=btime%1000000000000
     btime=str(btime)
     print(btime)

     price=request.form['price']
     price=float(price)
     price=math.ceil(price)
     
     squery='''
     INSERT INTO reservation.seats
     VALUES
     (%s,%s)
     '''

     idshowing=request.form['idshowing']

     selected=''

     for seat in seats:
         if seat!='':
          booked.append(seat)
          selected=selected+seat+' '
          cursor = mysql.connection.cursor()
          cursor.execute(squery,[seat,idshowing])
          mysql.connection.commit()
          cursor.close() 


     num=len(booked)

     query='''
    SELECT *
    FROM reservation.user_account
    WHERE user_id=%s'''

     status='''
    SELECT *
    FROM reservation.showing
    WHERE idShowing=%s'''

     reservation='''
     INSERT INTO reservation.reservation
     VALUES
     (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
     '''

     user_id=session['google_id']

     cursor = mysql.connection.cursor()
     cursor.execute(query,[user_id])
     uid=cursor.fetchone()
     cursor.close()  

     cursor = mysql.connection.cursor()
     cursor.execute(status,[idshowing])
     status=cursor.fetchone()
     cursor.close()  
     
     time=status[1]

     date=status[3]

     screen=status[4]
     screen=int(screen)

     theatre=status[5]

     title=status[6]

     reservation_id=idshowing+btime

     price=125*num

     cursor = mysql.connection.cursor()
     cursor.execute(reservation,[btime,num,120,1,idshowing,screen,theatre,title,user_id,selected])
     mysql.connection.commit()
     cursor.close()  


     html='''
     <body style="margin: 0 !important; padding: 0 !important; background-color: #eeeeee;" bgcolor="#d537fd">
       <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: Open Sans, Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
    
       </div>
       <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td align="center" style="background-color: #eeeeee;" bgcolor="#eeeeee">
                <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
                    <tr>
                        <td align="center" valign="top" style="font-size:0; padding: 35px;" bgcolor="#000000">
                            <div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;">
                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;">
                                    <tr>
                                        <td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 36px; font-weight: 800; line-height: 48px;" class="mobile-center">
                                            <h1 style="font-size: 36px; font-weight: 800; margin: 0; color: rgb(255, 255, 255);">Cine Show</h1>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                            <div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;" class="mobile-hide">
                                <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;">
                                    <tr>
                                        <td align="right" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; line-height: 48px;">
                                            <table cellspacing="0" cellpadding="0" border="0" align="right">
                                                <tr>
                                                    <td style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400;">
                                                        <p style="font-size: 18px; font-weight: 400; margin: 0; color: #ffffff;"><a href="#" target="_blank" style="color: #ffffff; text-decoration: none;">Shop &nbsp;</a></p>
                                                    </td>
                                                    <td style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 24px;"> <a href="#" target="_blank" style="color: #ffffff; text-decoration: none;"><img src="https://img.icons8.com/color/48/000000/small-business.png" width="27" height="23" style="display: block; border: 0px;" /></a> </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 35px 35px 20px 35px; background-color: #ffffff;" bgcolor="#ffffff">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
                                <tr>
                                    <td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 25px;"> <img src="https://img.icons8.com/carbon-copy/100/000000/checked-checkbox.png" width="125" height="120" style="display: block; border: 0px;" /><br>
                                        <h2 style="font-size: 30px; font-weight: 800; line-height: 36px; color: #333333; margin: 0;"> Thank You For Your Booking! </h2>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 10px;">
                                        <p style="font-size: 16px; font-weight: 400; line-height: 24px; color: #777777;"></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding-top: 20px;">
                                        <table cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="75%" align="left" bgcolor="#eeeeee" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px;"> Order Confirmation # </td>
                                                <td width="25%" align="left" bgcolor="#eeeeee" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px;">'''+ str(reservation_id)+ '''</td>
                                            </tr>
                                            <tr>
                                                <td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 15px 10px 5px 10px;">''' + title+'''('''+str(num)+''') </td>
                                                <td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 15px 10px 5px 10px;"> Rs.'''+str(price)+'''</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding-top: 20px;">
                                        <table cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> TOTAL </td>
                                                <td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> Rs.''' + str(price)+'''</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" height="100%" valign="top" width="100%" style="padding: 0 35px 35px 35px; background-color: #ffffff;" bgcolor="#ffffff">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:660px;">
                                <tr>
                                    <td align="center" valign="top" style="font-size:0;">
                                        <div style="display:inline-block; max-width:50%; min-width:240px; vertical-align:top; width:100%;">
                                            <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;">
                                                <tr>
                                                    <td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px;">
                                                        <p style="font-weight: 800;">Screen Number</p>
                                                        <p>''' +str(screen)+'''</p>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px;">
                                                        <p style="font-weight: 800;">Ticket Number</p>
                                                        <p>''' +str(selected)+'''</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                        <div style="display:inline-block; max-width:50%; min-width:240px; vertical-align:top; width:100%;">
                                            <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;">
                                                <tr>
                                                    <td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px;">
                                                        <p style="font-weight: 800;">Show Date</p>
                                                        <p>'''+ str(date)+''' '''+str(time)+'''</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style=" padding: 35px; background-color: #000000;" bgcolor="#d537fd">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
                                <tr>
                                    <td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 25px;">
                                        <h2 style="font-size: 24px; font-weight: 800; line-height: 30px; color: #ffffff; margin: 0;"> Cine Show </h2>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" style="padding: 25px 0 15px 0;">
                                        <table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="center" style="border-radius: 5px;" bgcolor="#66b3b7"> <a href="#" target="_blank" style="font-size: 18px; font-family: Open Sans, Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; border-radius: 5px; background-color: #F44336; padding: 15px 30px; border: 1px solid #F44336; display: block;">Book Again</a> </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 35px; background-color: #ffffff;" bgcolor="#ffffff">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
                                <tr>
                                    
                                </tr>
                               
                                <tr>
                                    <td align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 24px;">
                                        <p style="font-size: 14px; font-weight: 400; line-height: 20px; color: #777777;"> If you didn't create an account using this email address, please ignore this email or <a href="#" target="_blank" style="color: #777777;">unsusbscribe</a>. </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
       </table>
     </body>'''

     mail.send_message('New message from ' + 'Cine Show', sender='Cine Show', recipients = [uid[1]], html=html)    
    
     return redirect('/confirmation')