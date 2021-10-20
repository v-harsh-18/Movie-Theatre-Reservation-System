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

def details1():
    return render_template('details1.html') 

def details2():
    return render_template('details2.html')          

def pricing():
    return render_template('pricing.html')     

def faq():
    return render_template('faq.html')     

def about():
    return render_template('about.html')         