from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

if __name__ == "__main__":
    contas = {}
    def criar_conta():
        try:
            nome = input("digite o nome da conta ")
            if nome in contas:
                raise ValueError("ja existe uma conta com esse nome")
            
            n = input("digite 1 para conta corrente\ndigite 2 para conta poupança ")
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
            valor = float(input("digite o valor a ser sacado. "))
            if valor <= 0:
                raise ValueError("o valor a ser sacado deve ser maior que 0")
            
            if not contas[nome].sacar(valor):
                raise ValueError("saldo insuficiente para saque.")
            else:
                print(f"saque de R${valor} realizado na conta {nome}")

        except ValueError as e:
            print(f"erro: {e}")


    def verificar_saldo():
        
        nome = input("digite o nome da conta ")
        if nome not in contas:
            raise ValueError("essa conta não existe")
        print(contas[nome])

    def transferir():
        try:
            nome1 = input("digite a conta de origem ")
            nome2 = input("digite a conta destino ")
            if nome1 not in contas or nome2 not in contas:
                raise ValueError("uma ou as duas contas não existem")
            valor = float(input("digite o valor a ser transferido "))
            if valor <= 0:
                raise ValueError("o valor a ser transferido deve ser maior que 0")
            
            if not contas[nome1].transferencia(valor,contas[nome2]):
                raise ValueError("saldo insuficiente para a transferência")
            else:
                print(f"pix de R${valor} realizado de {nome1} para {nome2}")

        except ValueError as e:
            print(f"erro: {e}")

    def aplicar_rendimento():
        try:
            nome = input("digite o nome da conta que deseja aplicar o rendimento ")
            if nome not in contas:
                raise ValueError("essa conta não existe.")
            contas[nome].render()
        except ValueError as e:
            print(f"erro: {e}")
        except Exception:
            print("Erro.")
    
    def comparar_contas():
        try:
            nome1 = input("digite o nome da conta a ser comparada ")
            nome2 = input("digite o nome da outra conta a ser comparada ")
            if nome1 not in contas or nome2 not in contas:
                raise ValueError("uma ou as duas contas não existem.")
            if contas[nome1] == contas[nome2]:
                print("as duas contas tem o mesmo saldo.")
            elif contas[nome1] < contas[nome2]:
                print(f"{nome2} tem mais saldo que {nome1}")
            else:
                print(f"{nome1} tem mais saldo que {nome2}.")
        except ValueError as e:
            print(f"erro: {e}")

        


    def menu():
        while True:
            print("---BANCO LIPE E MOÉSIO---\n1- criar conta\n2- depositar\n3- sacar\n4- verificar saldo\n5- pix\n6- aplicar rendimento (conta poupança)\n7- comparar contas\n8- sair")
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
                    transferir()
                elif escolha == "6":
                    aplicar_rendimento()
                elif escolha == "7":
                    comparar_contas()
                elif escolha == "8":
                    print("---Até a próxima, volte sempre!!---")
                    break
                else: 
                    raise ValueError("digite um numero de 1 a 8")
            except ValueError as e:
                print(f"erro: {e}")
    menu()