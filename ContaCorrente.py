from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor):
        taxa = 1
        valor_total = valor + taxa

        if valor_total <= self.get_saldo():
            super().sacar(valor_total)
            print(f"Taxa de R$ {taxa:.2f} cobrada.")
        else:
            print("Operação recusada! Saldo insuficiente para saque + taxa.")