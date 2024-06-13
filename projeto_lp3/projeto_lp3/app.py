from flask import Flask

# Jeito errado de fazer:
# from validate_docbr import CPF # importa a classe CPF
# from validate_docbr import CNPJ # importa a classe CNPJ

# Jeito correto de fazer:
from validate_docbr import CNPJ, CPF 

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

@app.route("/produtos")
def Produtos():
    return "<h1>Produtos<h1>"

# criar uma página /servicos retornar "nossos serviços" (colar oq ja tem)
# página /gerar-cpf retornar cpf aleatório (usar a biblioteca do cpf que instalamos)
# página /gerar cnpj e retornar Cnpj aleatório (usar a mesma biblioteca de cima) 

@app.route("/servicos")
def servicos():
    return "<h1> Nossos serviços <h1>" # devolve HTML como STring, péssima pratica


@app.route("/cpf")
def gerarCpf():
    cpf = CPF() # pode colocar dentro ou fora da função
    return cpf.generate(True)

@app.route("/cnpj")
def gerarCnpj():
    cnpj = CNPJ() # objeto do tipo CNPJ
    return cnpj.generate(True)

app.run()

