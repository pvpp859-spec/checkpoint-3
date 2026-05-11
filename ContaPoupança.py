from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def render_juros(self):
        juros = self.get_saldo() * 0.01
        self.depositar(juros)
        print("Juros de 1% aplicados.")