from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, cpf, senha=None, saldo=0, taxa_rendimento = 0.05):
        super().__init__(titular, cpf, senha, saldo)
        self.__taxa_rendimento = taxa_rendimento

    def depositar(self, valor,):
        self.set_saldo(self.get_saldo() + valor)
        return True
    
    def sacar(self, valor):
        try:
            if valor > self.get_saldo():
                raise ValueError("Saldo insuficiente para saque.")
            self.set_saldo(self.get_saldo() - valor)
            return True
        except ValueError as e:
            print(f"Erro ao sacar: {e}")
    
    def render(self):
        try:
            if self.get_saldo() == 0:
                raise ValueError("não há rendimento em conta sem saldo, por favor deposite.")
            rendimento = self.get_saldo()*self.__taxa_rendimento    
            self.depositar(rendimento)
            print(f"foi aplicado um rendimento de R${rendimento}")

        except ValueError as e:
            print(f"erro: {e}")
                




