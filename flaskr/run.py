#!/usr/bin/python

import sys

sys.path.append("/home/jzhu/my-website-by-flask/flaskr")

from app import app
from app import views
from app import models
from app import db
app.run(debug = True)
