from flask import Flask, render_template, request, redirect, url_for
from models import db, Conta, Lancamento

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contabilidade.db'
app.config['SECRET_KEY'] = 'secreto'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contas', methods=['GET', 'POST'])
def contas():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        nova_conta = Conta(nome=nome, tipo=tipo)
        db.session.add(nova_conta)
        db.session.commit()
        return redirect(url_for('contas'))
    contas = Conta.query.all()
    return render_template('contas.html', contas=contas)

@app.route('/lancamentos', methods=['GET', 'POST'])
def lancamentos():
    if request.method == 'POST':
        conta_debito = request.form['conta_debito']
        conta_credito = request.form['conta_credito']
        valor = float(request.form['valor'])
        novo_lancamento = Lancamento(conta_debito=conta_debito, conta_credito=conta_credito, valor=valor)
        db.session.add(novo_lancamento)
        db.session.commit()
        return redirect(url_for('lancamentos'))
    lancamentos = Lancamento.query.all()
    contas = Conta.query.all()
    return render_template('lancamentos.html', lancamentos=lancamentos, contas=contas)

@app.route('/balancete')
def balancete():
    contas = Conta.query.all()
    return render_template('balancete.html', contas=contas)

if __name__ == '__main__':
    app.run(debug=True)
