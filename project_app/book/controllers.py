from flask import Blueprint #plano

bookBp = Blueprint('book',__name__) #nombre de la ruta

#Creamos la ruta y una funcion simple
@bookBp.route('/')
def index():
    return 'hola mundo'