from flask import Flask,render_template

app=Flask(__name__)
@app.route('/') 
def Inicio():
    return render_template('index.html', titulo_pagina = 'Home')

@app.route('/produtos')
def listar():
    return render_template('produtos.html', titulo_pagina = 'Produtos')

@app.route('/maisvendidos')
def cadastrar():
    return render_template('maisvendidos.html', titulo_pagina = 'Mais Vendidos')

@app.route('/atendimentoaocliente')
def atendimentoaocliente():
    return render_template('atendimentoaocliente.html', titulo_pagina = 'Atendimento ao Cliente')


app.run()