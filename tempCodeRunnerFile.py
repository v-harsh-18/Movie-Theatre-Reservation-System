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
app.config['MYSQL_DB'] = 'faculty_assignment'
app.config['UPLOAD_FOLDER'] = 'static/files'