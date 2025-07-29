# ocultação de detalhes internos de um objeto.
class Conta:
    def __init__(self, agencia = "", saldo = 0):
        self._saldo = saldo
        self.agencia = agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor


conta = Conta("0033", 100)
conta.depositar(100)
print(f"Saldo da conta: {conta._saldo}")
