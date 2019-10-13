from flask import Flask, render_template,request,redirect
from models.investimento import Investimento


app = Flask(__name__)
titulo = "Investimentos"

@app.route('/')
def inicio():
    return render_template('index.html', titulo = titulo)

@app.route('/fixa')
def fixa():
    return render_template('fixa.html', titulo = titulo)

@app.route('/variavel')
def variavel():
    return render_template('variavel.html', titulo = titulo)

@app.route('/saiba_mais')
def saiba_mais():
    return render_template('saiba_mais.html', titulo = titulo)

@app.route('/salvar_fixa', methods=['POST'])
def salvar_fixa():
    quantidade = request.form[quantidade]
    tipo = request.form[tipo]
    aporte = request.form[aporte]
    rentabilidade = request.form[rentabilidade]
    rentabilidade_mensal = request.form[rentabilidade_mensal]
    rentabilidade_anual = request.form[rentabilidade_anual]
    periodo = request.form[periodo]
    novo_investimento = Investimento(quantidade,tipo,aporte,rentabilidade,rentabilidade_mensal,rentabilidade_anual,periodo)
    novo_investimento.append()
    return redirect('/listar')

@app.route('/salvar_variavel', methods=['POST'])
def salvar_variavel():
    quantidade = request.form[quantidade]
    tipo = request.form[tipo]
    aporte = request.form[aporte]
    rentabilidade = request.form[rentabilidade]
    rentabilidade_mensal = request.form[rentabilidade_mensal]
    rentabilidade_anual = request.form[rentabilidade_anual]
    periodo = request.form[periodo]
    novo_investimento = Investimento(quantidade,tipo,aporte,rentabilidade,rentabilidade_mensal,rentabilidade_anual,periodo)
    novo_investimento.append()
    return redirect('/listar')

app.run() 