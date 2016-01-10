#!/usr/bin/python

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    name = db.Column(db.String(120))
    test1 = db.Column(db.String(120))
    test2 = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Entries(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), index = True, unique = True)
    text = db.Column(db.String(20000))

    def __repr__(self):
        return '<Entries %r>' % (self.title)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
