class Conta:
    def __init__(self, titular, cpf, senha, saldo=0,):
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
        return "\n" + "-"*10 + f"SALDO ATUAL - R$ {self.__saldo:.2f} ".center(30) + "-"*10

    def transferencia(self, valor, destino):
        try:
            if valor > self.__saldo:
                raise ValueError("Saldo insuficiente para a transferencia.")
            self.__saldo -= valor
            destino.depositar(valor)
            return True
        except ValueError as e:
            print(f"❌ Erro: {e}")

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