from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    mail = db.Column(db.String(60))
    telefono = db.Column(db.String(15))