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

#Configuracion modo debug
app.debug = True

#cargando la configuracion con MongoEngine
db = MongoEngine(app)

# Controladores
# Registramos la ruta de la funcion index de nuestro controlador
from project_app.book.controllers import bookBp
app.register_blueprint(bookBp) 

