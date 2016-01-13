#import sys
#sys.path.append("/home/jzhu/my-website-by-flask/flaskr")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
from flask_admin import Admin
# Flask and Flask-SQLAlchemy initialization here
admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Post, db.session))
