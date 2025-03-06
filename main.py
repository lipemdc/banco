from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


contas = {}
conta_logada = None
def criar_conta():
    print("\n" + "="*50)
    print("🆕 CRIAR NOVA CONTA 🆕".center(50))
    print("="*50)

    while True:
        nome = input("\n◀️  Digite (voltar) para retornar ao menu \n" +
                    "📝 Nome do titular (apenas letras)\n>")
        if nome.lower() == "voltar":
            return
        
        try:   
            if not nome.replace(' ', '').isalpha():
                raise ValueError("O nome deve conter apenas letras ")
            break

        except ValueError as e:
            print(f"❌ Erro: {e}")

    while True:
        senha = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                      "🔐 Crie uma senha (mínimo 6 caracteres, letras e números)\n> ")
        if senha.lower() == "voltar":
            return
        
        try:   
            if len(senha) < 6:
                raise ValueError("Sua senha deve ter no mínimo 6 caracteres.")
            
            if senha.isdigit() or senha.isalpha():
                raise ValueError("Sua senha deve conter letras e números.")
            break

        except ValueError as e:
            print (f"❌ Erro: {e}")

    
    while True:
        cpf = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                      "🆔 Digite seu CPF (11 dígitos)\n> ")
        if cpf.lower() == "voltar":
            return
        
        try:
            if len(cpf) != 11:
                raise ValueError("Seu CPF deve ter 11 digitos. Apenas números.")
            if not cpf.isdigit():
                raise ValueError("Seu CPF deve conter apenas numeros.")
            
            if cpf in contas:
                raise ValueError("CPF ja cadastrado")
            break

        except ValueError as e:
            print (f"❌ Erro: {e}")


    while True:
        tipo = input("\n◀️  Digite (voltar) para voltar\n" +
                    "📋 Selecione o tipo da conta:\n"
                    "[1] Conta Corrente\n"
                    "[2] Conta Poupança\n> ")

        if tipo.lower() == "voltar":
            return
        
        try:
            if tipo == "1": 
                contas[cpf] = ContaCorrente(nome,cpf,senha)
                tipo = "Corrente"

            elif tipo == "2":
                contas[cpf] = ContaPoupanca(nome,cpf,senha)
                tipo = "Poupança"
           
            else:
                raise ValueError("Entrada inválida! Digite 1 ou 2.")
            break

        except ValueError as e:
            print (f"❌ Erro: {e}")
    print("\n" + "-"*50)
    print(f"✅ Conta {tipo} criada no nome de {nome}.".center(50))
    print("-"*50)
             

def depósito():
    global conta_logada

    print("\n" + "="*50)
    print("💰 DEPÓSITO 💰".center(50))
    print("="*50)

    while True:
        valor = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                    "💵 Digite o valor a ser depositado:\n>R$ ")
        if valor.lower() == "voltar":
            return

        try:
            valor_float = float(valor)
            if valor_float <= 0:
                raise ValueError
            
            conta_logada.depositar(valor_float)
            print("\n" + "-"*50)
            print(f"✅ Depósito de R$ {valor_float:.2f} realizado com sucesso!".center(50))
            print("-"*50)
            return
        
        except ValueError:
            print("❌ Erro: Por favor, digite um valor numérico válido maior que zero.")
        

def saque():
    global conta_logada

    print("\n" + "="*50)
    print("💰 SAQUE 💰".center(50))
    print("="*50)

    while True:
        valor = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                    "💵 Digite o valor a ser sacado:\n>R$ ")
        if valor.lower() == "voltar":
            return
        
        try:
            valor_float = float(valor)
            if valor_float <= 0:
                raise ValueError
            
            if conta_logada.sacar(valor_float):
                print("\n" + "-"*50)
                print(f"✅ Saque de R$ {valor_float:.2f} realizado com sucesso!".center(50))
                print("-"*50)
                return
            
        except ValueError:
            print("❌ Erro: Por favor, digite um valor numérico válido maior que zero.")
             


def verificar_saldo():
    print(conta_logada)

    

def transferir():
    global conta_logada

    print("\n" + "="*50)
    print("💰 PIX 💰".center(50))
    print("="*50)

    while True:
        cpf = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                      "🆔 Digite o CPF da conta destino\n> ")
        if cpf.lower() == "voltar":
            return
        
        try:
            if cpf not in contas:
                raise ValueError("a conta destino não existe")
            break

        except ValueError as e:
            print(f"❌ Erro: {e}")

    while True:
        valor = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                        "💵 Digite o valor a ser transferido:\n>R$ ")
        if valor.lower() == "voltar":
            return
        
        try:
            valor_float = float(valor)
            if valor_float <= 0:
                raise ValueError
            
            if conta_logada.transferencia(valor_float,contas[cpf]):
                print("\n" + "-"*50)
                print(f"✅ Pix R$ {valor_float:.2f} para {contas[cpf].get_titular()} realizado com sucesso!".center(50))
                print("-"*50)
                return 
                
        except ValueError:
            print("❌ Erro: Por favor, digite um valor numérico válido maior que zero.")
            

def aplicar_rendimento():
    global conta_logada
    try: 
        if isinstance(conta_logada, ContaPoupanca):
            conta_logada.render()
        else:
            raise ValueError("apenas conta poupança possui rendimento.")
        
    except ValueError as e:
        print(f"❌ Erro: {e}")
    

def comparar_contas():
    print("\n" + "="*50)
    print("💰 COMPARAR CONTAS 💰".center(50))
    print("="*50)

    while True:
        try:
            cpf1 = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                        "🆔 CPF da primeira conta\n> ")
            if cpf1.lower() == "voltar":
                return
            
            if cpf1 not in contas:
                raise ValueError("cpf incorreto, essa conta não existe")
            
            cpf2 = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                        "🆔 CPF da segunda conta\n> ")
            if cpf2.lower() == "voltar":
                return
            
            if cpf2 not in contas:
                raise ValueError("cpf incorreto, essa conta não existe.")
                
            if contas[cpf1] == contas[cpf2]:
                print("\n✅ As duas contas têm o mesmo saldo.")
                return
            
            elif contas[cpf1] < contas[cpf2]:
                print(f"\n🔍 {contas[cpf2].get_titular()} tem mais saldo que {contas[cpf1].get_titular()}")
                return
            
            else:
                print(f"\n🔍 {contas[cpf1].get_titular()} tem mais saldo que {contas[cpf2].get_titular()}.")
                return
            
        except ValueError as e:
            print(f"❌ Erro: {e}")

def login():
    global conta_logada

    print("\n" + "="*50)
    print("🔐 LOGIN 🔐".center(50))
    print("="*50)
    
    while True:
        cpf = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                "🆔 Digite seu CPF\n> ")
        if cpf.lower() == "voltar":
            return
        
        try:
            if cpf not in contas:
                raise ValueError("essa conta não existe ")
            break

        except ValueError as e:
            print(f"❌ Erro: {e}")
            
    while True:
        try:
            senha = input("\n◀️  Digite (voltar) para retornar ao menu \n" + 
                      f"🔑 Digite a senha da conta {contas[cpf].get_titular()}\n> ")
            if senha.lower() == "voltar":
                return
            
            elif senha != contas[cpf].get_senha():
                raise ValueError("Senha incorreta")
            
            conta_logada = contas[cpf]
            print("Login efetuado com sucesso")
            return
        
        except ValueError as e:
            print(f"❌ Erro: {e}")

def logout():
    global conta_logada
    conta_logada = None

def menu():
    while True:
        if conta_logada:
            print("\n" + "="*50)
            print(f"📌 CONTA DE {conta_logada.get_titular().upper()} 📌".center(50))
            print("="*50)
            print("\n📌 Escolha uma opção:\n")
            print("   [1] 💰 Depositar")
            print("   [2] 💸 Sacar")
            print("   [3] 📊 Verificar saldo")
            print("   [4] 🔄 Pix")
            print("   [5] 📈 Aplicar rendimento (Conta Poupança)")
            print("   [6] ❌ voltar")
            print("\n" + "="*50)

            while True:
                try:    
                    escolha = input("\n🤔 O que deseja fazer? ")
                    if escolha == "1":
                        depósito()
                        break
                    elif escolha == "2":
                        saque()
                        break
                    elif escolha == "3":
                        verificar_saldo()
                        break
                    elif escolha == "4":
                        transferir()
                        break
                    elif escolha == "5":
                        aplicar_rendimento()
                        break
                    elif escolha == "6":
                        logout()
                        break

                    else:
                        raise ValueError("Digite um numero de 1 a 6")
                except ValueError as e:
                    print(f"❌ Erro: {e}")
        else: 
            print("\n" + "="*50)
            print("🏦 BEM-VINDO AO BANCO LIPE E MOISÉS 🏦".center(50))
            print("="*50)
            print("   [1] 🚪 Login")
            print("   [2] 🆕 Criar conta")
            print("   [3] 🏦 Comparar contas")
            print("   [4] ❌ Sair")
            print("\n" + "="*50)

            while True:
                try:
                    escolha = input("\n🤔 O que deseja fazer? ")
                    if escolha == "1":
                        login()
                        break
                    elif escolha == "2":
                        criar_conta()
                        break
                    elif escolha == "3":
                        comparar_contas()
                        break
                    elif escolha =="4":
                        sair = input("🔄 Você está prestes a sair do banco! Digite (S) para confirmar ou qualquer outra tecla para continuar no sistema: ")
                        if sair.lower() == "s":
                            print("\n" + "="*50)
                            print("🏦 Obrigado por usar o Banco Lipe e Moisés! 🏦".center(50))
                            print("     🙌 Até a próxima, volte sempre! 🙌".center(50))
                            print("="*50 + "\n")
                            return
                        else:
                            break
                    else:
                        raise ValueError("Digite um numero de 1 a 4.")
                except ValueError as e:
                    print(f"❌ Erro: {e}")

if __name__ == "__main__":
    menu()
    