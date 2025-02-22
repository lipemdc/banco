from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

if __name__ == "__main__":
    contas = {}
    def criar_conta():
        try:
            nome = input("digite o nome da conta ")
            if nome in contas:
                raise ValueError("ja existe uma conta com esse nome")
            
            n = input("digite 1 para conta corrente\ndigite 2 para conta poupança")
            if n == "1":
                contas[nome] = ContaCorrente(nome)
                tipo = "corrente"

            elif n == "2":
                contas[nome] = ContaPoupanca(nome)
                tipo = "poupança"
            else:
                raise ValueError("escolha inválida! digite 1 ou 2.")
            
            print(f"conta {tipo} criada no nome de {nome}") 

        except ValueError as e:
            print(f"Erro: {e}")

    def depósito():
        try:
            nome = input("digite o nome da conta ")
            if nome not in contas:
                raise ValueError("essa conta não existe")
            valor = float(input("digite o valor a ser depositado "))
            if valor <= 0:
                raise ValueError("o valor a ser depositado deve ser maior que 0")
            
            contas[nome].depositar(valor)
            print(f"o valor de R${valor} foi depositado à conta {nome}")

        except ValueError as e:
            print(f"erro: {e}")

    def saque():
        try:
            nome = input("digite o nome da conta ")
            if nome not in contas:
                raise ValueError("essa conta não existe")
            valor = float(input("digite o valor a ser sacado."))
            if valor <= 0:
                raise ValueError("o valor a ser sacado deve ser maior que 0")
            
            saque = contas[nome].sacar(valor)
            if saque == False:
                raise ValueError("saldo insuficiente para saque")
            else:
                print(f"saque de R${valor} realizado na conta {nome}")

        except ValueError as e:
            print(f"erro:{e}")

    def verificar_saldo():
        nome = input("digite o nome da conta")
        if nome not in contas:
            raise ValueError("essa conta não existe")
        print(contas[nome])

    def menu():
        while True:
            print("---BANCO LIPE---\n1- criar conta\n2- depositar\n3- sacar\n4- verificar saldo\n5- sair")
            try:    
                escolha = input("oque deseja fazer?")
                if escolha == "1":
                    criar_conta()
                elif escolha == "2":
                    depósito()
                elif escolha == "3":
                    saque()
                elif escolha == "4":
                    verificar_saldo()
                elif escolha == "5":
                    print("---Até a próxima, volte sempre!!---")
                    break
                else: 
                    raise ValueError("digite um numero de 1 a 4")
            except ValueError as e:
                print(f"erro: {e}")


    menu()