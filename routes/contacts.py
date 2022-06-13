from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new')
def new():
    return render_template('index.html')

@contacts.route('/getall')
def getall():
    return render_template('index.html')

@contacts.route('/update')
def update():
    return render_template('index.html')

@contacts.route('/delete')
def delete():
    return render_template('index.html')