from flask import url_for
from app import db

class Officer(db.Document):
    firstName = db.StringField(max_length=255, required=True)
    lastName = db.StringField(max_length=255, required=True)
    employeeNum = db.IntField()
    email = db.EmailField()
    address1 = db.StringField(max_length=255, required=False)
    address2 = db.StringField(max_length=255, required=False)
    city = db.StringField(max_length=255, required=False)
    state = db.StringField(max_length=255, required=False)
    zip = db.StringField(max_length=255, required=False)
    phone = db.StringField(max_length=255, required=False)
    rank = db.StringField(max_length=255, required=False)
    active = db.BooleanField(required=True)
    armed = db.BooleanField(required=True)
    customerID = db.StringField(max_length=255, required=True)
