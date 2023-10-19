from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

class ContaBancaria:
    saldo = 0

    checar_saldo = lambda self: f"Saldo atual: {self.saldo}"

    depositar = lambda self, valor: setattr(self, 'saldo', self.saldo + valor) or f"Depósito de {valor} realizado. Saldo atual: {self.saldo}"

    sacar = lambda self, valor: (setattr(self, 'saldo', self.saldo - valor) or f"Retirada de {valor} realizada. Saldo atual: {self.saldo}") if self.saldo >= valor else "Retirada não permitida"

conta = ContaBancaria()

index = lambda : render_template_string('''
<form method="post">
    Valor: <input type="number" name="valor">
    <input type="submit" name="acao" value="Depositar">
    <input type="submit" name="acao" value="Sacar">
</form>
<p>{{ mensagem }}</p>
''', mensagem=request.form.get('acao') and (conta.depositar(float(request.form.get('valor'))) if request.form.get('acao') == 'Depositar' else conta.sacar(float(request.form.get('valor')))) or conta.checar_saldo())

app.add_url_rule("/", view_func=index, methods=["GET", "POST"], endpoint="index")

app.run(debug=True)