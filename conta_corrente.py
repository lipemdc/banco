from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular,saldo)
        self.__limite = limite
    
    def depositar(self, valor):
        try:
            if valor <= 0:
                raise ValueError("O valor a ser depositado deve ser maior que 0.")
            self.set_saldo(self.get_saldo() + valor)
        except ValueError as e:
            print(f"Erro ao depositar: {e}")

    def sacar(self, valor):
        try:
            if valor > self.__limite + self.get_saldo():
                raise ValueError("Saldo insuficiente para saque, o limite foi excedido.")
            elif valor <= 0:
                raise ValueError("O valor a ser sacado deve ser maior que 0")
            elif valor > 0 and valor <= self.get_saldo() + self.__limite:
                self.set_saldo(self.get_saldo() - valor)
            return True

        except ValueError as e:
            print(f"Erro ao sacar: {e}")
            return False

    def get_limite(self):
        return self.__limite
    
    def set_limite(self, novo_limite):
        if novo_limite < 0:
            raise ValueError("o limite deve ser maior que 0")
        self.__limite = novo_limite