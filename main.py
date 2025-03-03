from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


contas = {}
conta_logada = None
def criar_conta():
    try:
        nome = input("digite o nome da conta ")
        if nome in contas:
            raise ValueError("ja existe uma conta com esse nome")
        
        senha = input("crie uma senha para sua conta (mínimo 4 caracteres.)")
        if len(senha) < 4:
            raise ValueError("sua senha deve ter no minimo 4 caracteres.")

        cpf = input("digite seu cpf.(11 digitos)")
        if len(cpf) != 11:
            raise ValueError("seu cpf deve ter 11 digitos.")
        if not cpf.isdigit():
            raise ValueError("o cpf deve conter apenas numeros.")


        n = input("digite 1 para conta corrente\ndigite 2 para conta poupança ")
        if n == "1":
            
            contas[cpf] = ContaCorrente(nome,cpf,senha)
            tipo = "corrente"

        elif n == "2":
            contas[cpf] = ContaPoupanca(nome,cpf,senha)
            tipo = "poupança"
        
        else:
            raise ValueError("escolha inválida! digite 1 ou 2.")

        print(f"conta {tipo} criada no nome de {nome}")
        print(f"{contas[cpf].get_senha()}") 

    except ValueError as e:
        print(f"Erro: {e}")           

def depósito():
    global conta_logada
    try:
        valor = float(input("digite o valor a ser depositado "))
        if valor <= 0:
            raise ValueError("o valor a ser depositado deve ser maior que 0")
          
        conta_logada.depositar(valor)
        print(f"o valor de R${valor} foi depositado à conta {conta_logada.get_titular()}")

    except ValueError as e:
        print(f"erro: {e}")
        

def saque():
    global conta_logada
    try:
        valor = float(input("digite o valor a ser sacado. "))
        if valor <= 0:
            raise ValueError("o valor a ser sacado deve ser maior que 0")
        
        
        if conta_logada.sacar(valor):
            print(f"saque de R${valor} realizado na conta {conta_logada.get_titular()}")

    except ValueError as e:
        print(f"erro: {e}")


def verificar_saldo():
    print(conta_logada)

    

def transferir():
    global conta_logada
    try:
        nome = input("digite a conta destino ")
        if nome not in contas:
            raise ValueError("a conta destino não existe")
        valor = float(input("digite o valor a ser transferido "))
        if valor <= 0:
            raise ValueError("o valor a ser transferido deve ser maior que 0")
        
        if conta_logada.transferencia(valor,contas[nome]):
            print(f"pix de R${valor} realizado para {nome}")
        else:
            raise ValueError("Saldo insuficiente para a transferência")

    except ValueError as e:
        print(f"erro: {e}")

def aplicar_rendimento():
    global conta_logada
    try: 
        if isinstance(conta_logada, ContaPoupanca):
            conta_logada.render()
        else:
            raise ValueError("apenas conta poupança possui rendimento.")
    except ValueError as e:
        print(f"erro: {e}")
    

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

def login():
    global conta_logada
    try:
        cpf = input("digite seu cpf ")
        if cpf not in contas:
            raise ValueError("essa conta não existe ")
        senha = input(f"digite a senha da conta {cpf}")
        if senha != contas[cpf].get_senha():
            raise ValueError("senha incorreta")
        conta_logada = contas[cpf]
        print("login efetuado com sucesso")

    except ValueError as e:
        print(f"erro: {e}")

def logout():
    global conta_logada
    conta_logada = None




def menu():
    while True:
        if conta_logada:
            print("\n" + "="*40)
            print(f"conta de {conta_logada.get_titular()} ")
            print("="*40)
            print("\n📌 Escolha uma opção:\n")
            print("   [1] 💰 Depositar")
            print("   [2] 💸 Sacar")
            print("   [3] 📊 Verificar saldo")
            print("   [4] 🔄 Pix")
            print("   [5] 📈 Aplicar rendimento (Conta Poupança)")
            print("   [6] ❌ voltar")
            print("\n" + "="*40)

            try:    
                escolha = input("\nO que deseja fazer? ")
                if escolha == "1":
                    depósito()
                elif escolha == "2":
                    saque()
                elif escolha == "3":
                    verificar_saldo()
                elif escolha == "4":
                    transferir()
                elif escolha == "5":
                    aplicar_rendimento()
                elif escolha == "6":
                    logout()

                else:
                    raise ValueError("digite um numero de 1 a 6")
            except ValueError as e:
                print(f"erro: {e}")
        
        else: 
            print("\n" + "="*40)
            print("🌟  BEM-VINDO AO BANCO LIPE E MOÉSIO  🌟")
            print("="*40)
            print("   [1] entrar")
            print("   [2] Criar conta")
            print("   [3] Comparar contas")
            print("   [4] sair")
            print("\n" + "="*40)

            try:
                escolha = input("oq quer fazer? ")
                if escolha == "1":
                    login()
                elif escolha == "2":
                    criar_conta()
                elif escolha == "3":
                    comparar_contas()
                elif escolha =="4":
                    print("\n" + "="*50)
                    print("✨ Obrigado por usar o Banco Lipe e Moésio! ✨")
                    print("     🙌 Até a próxima, volte sempre! 🙌")
                    print("="*50 + "\n")
                    break
                else:
                    raise ValueError("digite um numero de 1 a 4.")
            except ValueError as e:
                print(f"erro: {e}")

if __name__ == "__main__":
    menu()
    