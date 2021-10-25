from flask import Flask,render_template,request,session,redirect,flash
import math
from textblob import TextBlob


def booki():
    if request.method=='POST':
     print(request.form.getlist('book'))
     return redirect('/confirmation')