from flask import Flask,render_template,request,session,redirect,flash
import math
from textblob import TextBlob
from flask_mysqldb import MySQL

import models.display as display

app=Flask(__name__)

app.add_url_rule('/', view_func=display.index, methods=['GET'])
app.add_url_rule('/index', view_func=display.index2, methods=['GET'])
app.add_url_rule('/details1', view_func=display.details1, methods=['GET'])
app.add_url_rule('/details2', view_func=display.details2, methods=['GET'])
app.add_url_rule('/catalog1', view_func=display.catalog1, methods=['GET'])
app.add_url_rule('/catalog2', view_func=display.catalog2, methods=['GET'])
app.add_url_rule('/pricing', view_func=display.pricing, methods=['GET'])
app.add_url_rule('/faq', view_func=display.faq, methods=['GET'])
app.add_url_rule('/about', view_func=display.about, methods=['GET'])
app.add_url_rule('/details2', view_func=display.details2, methods=['GET'])
 
app.run(debug=True)
