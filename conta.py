class Conta:
    def __init__(self, titular, cpf, senha=None, saldo=0,):
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha
        self.__cpf = cpf

    def depositar(self, valor):
        pass
    
    def sacar(self, valor):
        pass

    def __eq__(self, outro):
        return self.__saldo == outro.__saldo

    def __lt__(self, outro):
        return self.__saldo < outro.__saldo
    
    def __str__(self):
        return f"Conta de {self.__titular} - Saldo: R$ {self.__saldo:.2f}"

    def transferencia(self, valor, destino):
        if valor <= 0:
            return False
        elif valor > self.__saldo:
            return False
        self.__saldo -= valor
        destino.depositar(valor)
        return True

    def aplicar_juros(self):
        pass  

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, novo_titular):
        self.__titular = novo_titular
        
    def get_saldo(self):
        return self.__saldo
        
    def set_saldo(self, valor):
        self.__saldo = valor

    def get_senha(self):
        return self.__senha
    
    def set_senha(self, nova_senha):
        self.__senha = nova_senha

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf