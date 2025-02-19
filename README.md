class Conta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        pass
    
    def sacar(self, valor):
        pass
    
    def __eq__(self, outro):
        return self.saldo == outro.saldo
    
    def __lt__(self, outro):
        return self.saldo < outro.saldo
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.titular} - Saldo: R$ {self.saldo:.2f}"

class ContaCorrente(Conta):
    def depositar(self, valor):
        if valor > 0: 
            self.saldo += valor
        else:
            raise ValueError("O valor a ser depositado deve ser um numero maior que 0.")
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.saldo -= valor

class ContaPoupanca(Conta):
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("O valor a ser depositado deve ser um numero maior que 0.")
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.saldo -= valor

if __name__ == "__main__":
    conta1 = ContaCorrente('Lipe', 150)
    conta2 = ContaPoupanca('Dudu', 700)
    
    conta1.depositar(350)
    conta2.sacar(200)
    print(conta1)
    print(conta2)
    
    print("saldo da Conta1 é igual o saldo da Conta2?", conta1 == conta2)
    print("saldo da Conta1 é menor que o saldo da Conta2?", conta1 < conta2)
