from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, taxa_rendimento = 0.05):
        super().__init__(titular, saldo)
        self.__taxa_rendimento = taxa_rendimento

    def depositar(self, valor,):
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
            return True
        except ValueError as e:
            print(f"Erro ao sacar: {e}")
    
    def render(self):
        try:
            if self.get_saldo() <= 0:
                raise ValueError("não há rendimento em conta sem saldo, por favor deposite.")
            rendimento = self.get_saldo()*self.__taxa_rendimento    
            self.depositar(rendimento)
            print(f"foi aplicado um rendimento de R${rendimento}")
        except ValueError as e:
            print(f"erro: {e}")
                




