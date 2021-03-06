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

app=Flask(__name__)
app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5792'
app.config['MYSQL_DB'] = 'reservation'

def login_is_required(function):
        if "google_id" not in session:
            return redirect('/login')
        else:
            return function()


def index():
    return render_template('index.html')

def index2():
    return render_template('index2.html')

def pricing():
    return render_template('pricing.html')    

def catalog1():
    return render_template('catalog1.html')  

def catalog2():
    return render_template('catalog2.html')  

def details2():
    return render_template('details2.html')          

def pricing():
    return render_template('pricing.html')     

def faq():
    return render_template('faq.html')     

def about():
    return render_template('about.html')      

def bell():
    return render_template('bell.html')  

def bhuj():
    return render_template('bhuj.html')               

def chehre():
    return render_template('chehre.html')  

def coolie():
    return render_template('collie.html')

def f9():
    return render_template('f9.html')  

def conjuring():
    return render_template('conjuring.html')    

def haseen():
    return render_template('haseen.html')  

def hellocharlie():
    return render_template('hellocharlie.html')     

def hungama2():
    return render_template('hungama2.html')  

def indoo():
    return render_template('indoo.html') 

def jagame():
    return render_template('jagame.html')  

def ludo():
    return render_template('ludo.html')     

def mimi():
    return render_template('mimi.html')  

def mumbaisaga():
    return render_template('mumbaisaga.html')         

def radhe():
    return render_template('radhe.html')  

def roohi():
    return render_template('roohi.html')   

def saina():
    return render_template('saina.html')  

def sherni():
    return render_template('sherni.html')      

def shershah():
    return render_template('shershah.html')  

def shiddat():
    return render_template('shiddat.html')        

def soorarai():
    return render_template('soorarai.html')  

def thailavi():
    return render_template('thailavi.html')           

def confirmation():
    return render_template('confirmation.html')

def dark():
    return render_template('dark.html')    

def moneyheist():
    return render_template('moneyheist.html')   

def mirzapur():
    return render_template('mirzapur.html')       

def familyman():
    return render_template('familyman.html')   

def squidgames():
    return render_template('squidgames.html')  

def narcos():
    return render_template('narcos.html')      

def theoriginals():
    return render_template('theoriginals.html')     

def kotafactory():
    return render_template('kotafactory.html')       

def sacredgames():
    return render_template('sacredgames.html')        

def patallok():
    return render_template('patallok.html')         

def fourmoreshots():
    return render_template('fourmoreshots.html')      

def scam():
    return render_template('scam.html') 

def tommorowwar():
    return render_template('tommorowwar.html')

def reminiscene():
    return render_template('reminiscene.html')