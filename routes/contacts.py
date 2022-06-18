from flask import Blueprint, render_template, request, redirect, url_for
from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

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

    new_contact = Contact(nombre, apellido, mail, telefono)
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

        db.session.commit()

        return redirect('/')
    
    return render_template('update.html', contact=contact)

@contacts.route('/delete/<id>')
def delete(id):
    
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    
    return redirect('/')