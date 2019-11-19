from app import app

# Criando uma rota no servidor para minha página
# Decorator antes da função para aplicar função em cima da outra função
@app.route('/')

def index():
    return 'Hello, World!'