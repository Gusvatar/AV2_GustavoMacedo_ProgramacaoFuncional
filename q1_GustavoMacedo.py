class ContaBancaria:
    saldo = 0

    checar_saldo = lambda self: f"Saldo atual: {self.saldo}"

    depositar = lambda self, valor: setattr(self, 'saldo', self.saldo + valor) or f"Depósito de {valor} realizado. Saldo atual: {self.saldo}"

    sacar = lambda self, valor: (setattr(self, 'saldo', self.saldo - valor) or f"Retirada de {valor} realizada. Saldo atual: {self.saldo}") if self.saldo >= valor else "Retirada não permitida"

conta = ContaBancaria()

# Exemplos
print(conta.depositar(500))
print(conta.sacar(200))
print(conta.sacar(1500))
print(conta.checar_saldo())
