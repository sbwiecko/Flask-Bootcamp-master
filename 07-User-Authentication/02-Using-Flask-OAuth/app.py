#######################################################################################
# Visit the Google Developers Console at https://console.developers.google.com        #
# and create a new project. In the "APIs & Services" section, click on "Credentials", #
# and then click the "Create Credentials" button. Select "OAuth Client Id" and        #
# "Desktop App" for the application type, and click the "Configure consent screen"    #
# button. Put in your application information, and click Save. Take note of the       #
# "Client ID" and "Client Secret" for the application. Alternatively, we can create   #
# a "Web Application" and click the "Configure consent screen" button. Put in         #
# your application information, and click Save. Once you've done that, you'll         #
# see two new fields: "Authorized JavaScript origins" and "Authorized redirect        #
# URIs". Put http://localhost:5000/login/google/authorized, but also                  #
# http://127.0.0.1:5000/login/google/authorized into "Authorized redirect URIs",      #
# and click "Create Client ID", otherwise will get an 400 error. Take note of the     #
# "Client ID" and "Client Secret" for the application.                                #
#######################################################################################


#######################################################################################
# IMPORTANT NOTE!!! HERE IS SOME CODE FOR THIS TO WORK LOCALLY YOU SHOULD ONLY NEED   #
# THIS CODE FOR LOCAL TESTING PLEASE REFER TO THE FLASK_DANCE DOCS FOR MORE INFO      #
# WINDOWS: set OAUTHLIB_INSECURE_TRANSPORT=1                                          #
# Macos/linux: export OAUTHLIB_INSECURE_TRANSPORT=1                                   #
# https://flask-dance.readthedocs.io/en/latest/quickstarts/google.html                #
#######################################################################################

import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'


from flask import Flask, redirect, url_for, render_template, session
from flask_dance.contrib.google import make_google_blueprint, google


app = Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'


blueprint = make_google_blueprint(
    client_id="424074174499-59dak07l4d24ts379m7jqr8hjvtfl0pd.apps.googleusercontent.com",
    client_secret="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",
    # reprompt_consent=True,
    offline=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/welcome')
def welcome():
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html", email=email)


# connection to the google blueprint
@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo") # check docs because it may change
    assert resp.ok, resp.text

    email=resp.json()["email"]

    return render_template("welcome.html", email=email)


if __name__ == "__main__":
    app.run()
