from flask import Flask,render_template,request,session,redirect,flash
import math
from textblob import TextBlob

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
 
app.run(debug=True)
