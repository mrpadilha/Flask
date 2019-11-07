# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from flask import Flask

# Criar a aplicação
app = Flask(__name__)

# Criando uma rota no servidor
@app.route('/')

def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='192.168.2.234', port='5000')