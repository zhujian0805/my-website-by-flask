#!/usr/bin/python

from app import db, models

u = models.User(nickname='admin', email='admin@emaisdfl.com')
db.session.add(u)
db.session.commit()

import datetime
u = models.User.query.get(7)
p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()
