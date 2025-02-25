class Conta:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

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
        try:
            if valor <= 0:
                raise ValueError("o valor a ser transferido deve ser maior que 0")
            elif valor > self.__saldo:
                raise ValueError("saldo insufiente para transferencia")
            
            self.__saldo -= valor
            destino.depositar(valor)
            return True
        except ValueError as e:
            print(f"erro ao transferir: {e}")
            
    def aplicar_juros(self):
        pass  
        
    def get_saldo(self):
        return self.__saldo
        
    def get_titular(self):
        return self.__titular
        
    def set_saldo(self, valor):
        self.__saldo = valor
    






