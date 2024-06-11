from flask import Flask

app = Flask("Minha App")

# rota + função

# Definição de rota
# / - home page  
@app.route("/")
def home():
    return "<h1>Home Page<h1>"

# /contato - página de contato 
@app.route("/contato")
def Contato():
    return "<h1>Contato<h1>"

# /produtos - pagina produtos 

@app.route("/Produtos")
def Produtos():
    return "<h1>Produtos<h1>"
