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
app.config['MYSQL_DB'] = 'faculty_assignment'

app.secret_key = 'your secret key'
 
mysql = MySQL(app)

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
    session["name"] = id_info.get("name")
    return redirect("/info")

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
app.add_url_rule('/booking', view_func=display.booking, methods=['GET'])
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
 
app.run(debug=True)
