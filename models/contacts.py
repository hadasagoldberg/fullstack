from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    mail = db.Column(db.String(60))
    telefono = db.Column(db.String(15))

    def __init__(self, nombre, apellido, mail, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono
