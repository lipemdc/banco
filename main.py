from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

if __name__ == "__main__":
    try:
        conta1 = ContaCorrente('Lipe', 150)
        conta2 = ContaPoupanca('Moises', 700)

        conta1.transferencia(100, conta2)
        conta2.sacar(10)
        
    except Exception as e:
        print(f"Erro inesperado: {e}")

    print(conta1)
    print(conta2)

    if conta1 == conta2:
        print("conta1 tem mais saldo que a conta2")
    elif conta1 < conta2:
        print("saldo da conta1 é menor que o saldo da conta2")
    else:
        print("saldo da conta2 é menor que o saldo da conta1")
        
    print("Saldo da Conta1 é igual ao saldo da Conta2?", conta1 == conta2)
    print("Saldo da Conta1 é menor que o saldo da Conta2?", conta1 < conta2)