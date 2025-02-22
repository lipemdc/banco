from conta import Conta

class ContaPoupanca(Conta):
    def depositar(self, valor):
        try:
            if valor <= 0:
                raise ValueError("O valor a ser depositado deve ser maior que 0.")
            self.set_saldo(self.get_saldo() + valor)
        except ValueError as e:
            print(f"Erro ao depositar: {e}")

    def sacar(self, valor):
        try:
            if valor > self.get_saldo():
                raise ValueError("Saldo insuficiente para saque.")
            elif valor <= 0:
                raise ValueError("O valor a ser sacado deve ser maior que 0")
            self.set_saldo(self.get_saldo() - valor)
        except ValueError as e:
            print(f"Erro ao sacar: {e}")
