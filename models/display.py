from flask import Flask,render_template,request,session,redirect,flash
import math
from textblob import TextBlob

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

def booking():
    seats={'A1','A9'}
    return render_template('booking.html',seats=seats)    

def bell():
    return render_template('bell.html')  

def bhuj():
    return render_template('bhuj.html')               

def chehre():
    return render_template('chehre.html')  

def coolie():
    return render_template('coolie.html')

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