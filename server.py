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
import models.booking as booking
from flask_mail import *
import datetime
import math

app=Flask(__name__)
app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5792'
app.config['MYSQL_DB'] = 'faculty_assignment'
app.config['UPLOAD_FOLDER'] = 'static/files'

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = '557691334506-90eceev7hjdanmsqke67dl0daaah0vj0.apps.googleusercontent.com'
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:5000/login/google/authorized"
)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5792'
app.config['MYSQL_DB'] = 'reservation'

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


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return redirect('/login')
        else:
            return function()

    return wrapper


@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route('/login/google/authorized')
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    
    user_id=id_info.get('sub')
    email=id_info.get('email')
    fname=id_info.get('given_name')
    lname=id_info.get('family_name')

    query='''
    SELECT *
    FROM reservation.user_account
    WHERE user_id=%s'''

    usid='''
    INSERT INTO reservation.user_account(user_id,fname,lname,email)
    VALUES(%s,%s,%s,%s)
    '''

    cursor = mysql.connection.cursor()
    cursor.execute(query,[user_id])
    uid=cursor.fetchone()
    cursor.close()

    if(uid==None):
        print(1)
        cursor = mysql.connection.cursor()
        cursor.execute(usid,[user_id,fname,lname,email])
        mysql.connection.commit()
        cursor.close()

    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.add_url_rule('/', view_func=display.index, methods=['GET'])
app.add_url_rule('/index', view_func=display.index2, methods=['GET'])
app.add_url_rule('/details2', view_func=display.details2, methods=['GET'])
app.add_url_rule('/catalog1', view_func=display.catalog1, methods=['GET'])
app.add_url_rule('/catalog2', view_func=display.catalog2, methods=['GET'])
app.add_url_rule('/pricing', view_func=display.pricing, methods=['GET'])
app.add_url_rule('/faq', view_func=display.faq, methods=['GET'])
app.add_url_rule('/about', view_func=display.about, methods=['GET'])
app.add_url_rule('/details2', view_func=display.details2, methods=['GET'])
app.add_url_rule('/booking', view_func=booking.booking, methods=['POST'])
app.add_url_rule('/f9', view_func=display.f9, methods=['GET'])
app.add_url_rule('/bell', view_func=display.bell, methods=['GET'])
app.add_url_rule('/bhuj', view_func=display.bhuj, methods=['GET'])
app.add_url_rule('/chehre', view_func=display.chehre, methods=['GET'])
app.add_url_rule('/coolie', view_func=display.coolie, methods=['GET'])
app.add_url_rule('/conjuring', view_func=display.conjuring, methods=['GET'])
app.add_url_rule('/haseen', view_func=display.haseen, methods=['GET'])
app.add_url_rule('/hellocharlie', view_func=display.hellocharlie, methods=['GET'])
app.add_url_rule('/hungama2', view_func=display.hungama2, methods=['GET'])
app.add_url_rule('/indoo', view_func=display.indoo, methods=['GET'])
app.add_url_rule('/jagame', view_func=display.jagame, methods=['GET'])
app.add_url_rule('/ludo', view_func=display.ludo, methods=['GET'])
app.add_url_rule('/mimi', view_func=display.mimi, methods=['GET'])
app.add_url_rule('/mumbaisaga', view_func=display.mumbaisaga, methods=['GET'])
app.add_url_rule('/radhe', view_func=display.radhe, methods=['GET'])
app.add_url_rule('/roohi', view_func=display.roohi, methods=['GET'])
app.add_url_rule('/saina', view_func=display.saina, methods=['GET'])
app.add_url_rule('/sherni', view_func=display.sherni, methods=['GET'])
app.add_url_rule('/shershah', view_func=display.shershah, methods=['GET'])
app.add_url_rule('/shiddat', view_func=display.shiddat, methods=['GET'])
app.add_url_rule('/soorarai', view_func=display.soorarai, methods=['GET'])
app.add_url_rule('/thailavi', view_func=display.thailavi, methods=['GET'])
app.add_url_rule('/confirmation', view_func=display.confirmation, methods=['GET']) 
app.add_url_rule('/book', view_func=booking.booked, methods=['POST'])
app.add_url_rule('/timings', view_func=booking.timings, methods=['POST','GET'])
app.add_url_rule('/dark', view_func=display.dark, methods=['GET']) 
app.add_url_rule('/familyman', view_func=display.familyman, methods=['GET']) 
app.add_url_rule('/fourmoreshots', view_func=display.fourmoreshots, methods=['GET']) 
app.add_url_rule('/kotafactory', view_func=display.kotafactory, methods=['GET']) 
app.add_url_rule('/mirzapur', view_func=display.mirzapur, methods=['GET']) 
app.add_url_rule('/moneyheist', view_func=display.moneyheist, methods=['GET']) 
app.add_url_rule('/narcos', view_func=display.narcos, methods=['GET']) 
app.add_url_rule('/patallok', view_func=display.patallok, methods=['GET']) 
app.add_url_rule('/sacredgames', view_func=display.sacredgames, methods=['GET']) 
app.add_url_rule('/scam', view_func=display.scam, methods=['GET']) 
app.add_url_rule('/squidgames', view_func=display.squidgames, methods=['GET']) 
app.add_url_rule('/theoriginals', view_func=display.theoriginals, methods=['GET']) 
app.add_url_rule('/tommorowwar', view_func=display.tommorowwar, methods=['GET']) 
app.add_url_rule('/reminiscene', view_func=display.reminiscene, methods=['GET']) 

if __name__=="__main__":
  app.run(debug=True)
