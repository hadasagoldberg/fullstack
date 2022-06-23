from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.contacts import Contact
from utils.db import db
from sqlalchemy import func, distinct,select
from flask_marshmallow import Marshmallow

contacts = Blueprint('contacts', __name__)

ma = Marshmallow(contacts)

class ContactsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'mail', 'telefono', 'pais')

contacts_schema = ContactsSchema()
contacts_schema = ContactsSchema(many = True)

@contacts.route('/')
def home():
    contacts = Contact.query.all()
    return render_template('index.html', contacts = contacts)

@contacts.route('/new', methods=['POST'])
def new():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    mail = request.form['mail']
    telefono = request.form['telefono']
    pais = request.form['pais']

    new_contact = Contact(nombre, apellido, mail, telefono,pais)
    db.session.add(new_contact)
    db.session.commit()

   
    return  redirect('/')
    

@contacts.route('/update/<id>', methods = ['GET', 'POST'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.nombre = request.form['nombre']
        contact.apellido = request.form['apellido']
        contact.mail = request.form['mail']
        contact.telefono = request.form['telefono']
        contact.pais = request.form['pais']
        
        db.session.commit()

        return redirect('/')
    
    return render_template('update.html', contact=contact)

@contacts.route('/delete/<id>')
def delete(id):
    
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    
    return redirect('/')

@contacts.route('/reporte')
def reporte():
    #reporte = db.session.query(func.count(distinct(Contact.pais)))
    #print(reporte)
    stmt = select([func.count(distinct(Contact.mail)), Contact.pais]).group_by(Contact.pais)
    consulta = db.session.execute(stmt).fetchall()
    return f"<p>Se muestra la cantidad de contactos de cada pais: {consulta}</p>"
