from flask import Flask, render_template

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
    return render_template("home.html") #tem q ter esse arquivo na pasta templates
    # render templates devolve qualquer arquivo, no caso é um arquivo HTML

# /contato - página de contato 
@app.route("/contato")
def Contato():
    return render_template("contato.html")

# /produtos - pagina produtos 

@app.route("/produtos")
def Produtos():
    lista_produtos = [ # cada produto é um dicionário
        { "nome": "Coca-cola", "descricao" : "mata a sede" }, 
        { "nome": "Doritos", "descricao" : "Suja a mão"},
        {  "nome": "Chocolate", "descricao" : "bom", }
    ]

    return render_template("produtos.html", produtos=lista_produtos) # cuidado para não repetir o nome da função na hora de criar uma lista


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

# layout
# só vai mudar onde estiver o block