#modulo en python

#Configuracion inicial http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
from flask import Flask
from flask_mongoengine import MongoEngine

"""
MongoEngine = es un conector de mongo al igual que pymoongo
"""

#instanciando flask
app = Flask(__name__)

#configuraciones de la base de datos 
app.config['MONGODB_SETTINGS'] = {
    'db' : 'flaskBootstrap'
}

#cargando la configuracion con MongoEngine
db = MongoEngine(app)