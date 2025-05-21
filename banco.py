menu = """[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair
=> """

saldo: int = 0
limite: int = 500
extrato: str = ""
numero_saques: int = 0
LIMITE_SAQUES: int = 3

while True:

    opc: str = input(menu)
    
    if opc.lower() == "d":
        valor: float = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opc.lower() == "s":
        valor: float = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opc.lower() == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opc.lower() == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
