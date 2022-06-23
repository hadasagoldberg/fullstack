from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    mail = db.Column(db.String(60), unique = True)
    telefono = db.Column(db.String(15))
    pais = db.Column(db.String(20))

    def __init__(self, nombre, apellido, mail, telefono,pais):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono
        self.pais = pais

    def to_json(consulta):
        return dict(
            cantidad = consulta.cantidad,
            pais = consulta.pais
        )


class Contactar(db.Model):
    dia = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.datetime.date(8))
    forma_contacto = db.Column(db.String(30))

    def __init__(self,dia,hora,forma_contacto):
        self.dia = dia
        self.hora = hora
        self.forma_contacto = forma_contacto

