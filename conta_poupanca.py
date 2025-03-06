from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, cpf, senha, saldo=0, taxa_rendimento = 0.05):
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
            print(f"❌ Erro: {e}")
    
    def render(self):
        try:
            if self.get_saldo() == 0:
                raise ValueError("Não há rendimento em conta sem saldo, por favor deposite.")
            rendimento = self.get_saldo()*self.__taxa_rendimento    
            self.depositar(rendimento)
            print("\n" + "-"*50)
            print(f"✅ Foi aplicado um rendimento de R${rendimento:.2f}".center(50))
            print("-"*50)

        except ValueError as e:
            print(f"❌ Erro: {e}")