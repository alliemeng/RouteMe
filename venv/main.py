import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def index():
    return render_template('purescribbledraw.html')

#@app.route('/drawroute')
#def drawroute():
#    db = get_db()
#    cur = db.execute('select longitude, latitude from coordinates')
#    coordinates = cur.fetchall()
#    return render_template('purescribbledraw.html')

#@app.route('/viewroute', methods=['POST', 'GET'])
#def viewroute():
#    db = get_db()
#    return render_template('purescribble.html')
