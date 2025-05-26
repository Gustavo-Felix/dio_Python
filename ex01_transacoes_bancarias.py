"""
Imagine que você trabalha no setor de TI de um banco e precisa criar um programa que registre as transações de uma conta bancária. 
Cada transação pode ser um depósito ou um saque, e todas elas serão armazenadas em uma lista. 
Seu programa deve calcular o saldo final da conta com base nas transações realizadas. 
Depósitos serão representados como valores positivos e saques como valores negativos.

Entrada
Uma lista contendo valores inteiros ou decimais representando as transações realizadas (ex.: [100, -50, 200]).

Valores positivos representam depósitos.
Valores negativos representam saques.
Saída
O saldo final da conta no formato: "Saldo: R$ X.XX"

"""


def calcular_saldo(transacoes):
    saldo = 0

    for transacao in transacoes:
        saldo += transacao
        
    return saldo
    

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

resultado = calcular_saldo(transacoes)

print(f'Saldo: R$ {resultado:.2f}')