#!/usr/bin/python
import sys
sys.path.append('/home/jzhu/my-website-by-flask/flaskr')
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import views, models
#import views, models
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
#from app import models
