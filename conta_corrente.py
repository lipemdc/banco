from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, cpf, senha, saldo=0, limite=500):
        super().__init__(titular, cpf, senha, saldo)
        self.__limite = limite
    
    def depositar(self, valor):
        self.set_saldo(self.get_saldo() + valor)
        return True

    def sacar(self, valor):
        try:
            if valor > self.__limite + self.get_saldo():
                raise ValueError("Saldo insuficiente para saque, o limite foi excedido.")
            
            self.set_saldo(self.get_saldo() - valor)
            return True
            
        except ValueError as e:
            print(f"❌ Erro: {e}")

    def get_limite(self):
        return self.__limite
    
    def set_limite(self, novo_limite):
        if novo_limite < 0:
            raise ValueError("o limite deve ser maior que 0")
        self.__limite = novo_limite
