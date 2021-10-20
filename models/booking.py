from flask import Flask,render_template,request,session,redirect,flash
import math
from textblob import TextBlob


def booking():
    return render_template('index.html')