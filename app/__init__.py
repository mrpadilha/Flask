# https://www.youtube.com/watch?v=MC7w6f2B7iU
# https://github.com/emkay-git/Camera-Doorbell-IOT
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# Importando do módulo app importando o app
from flask import Flask 

# Criar a aplicação - App é a instância da classe Flask que recebe a variável __name__
app = Flask(__name__)

from app.controllers import default

