"""
Você foi solicitado a criar um programa que analise uma lista de transações bancárias e filtre apenas aquelas que ultrapassam um valor limite. 
Seu programa deve retornar uma nova lista contendo somente as transações cujo valor absoluto (ignorar sinal negativo) seja maior que o limite informado.

Atenção:
As transações incluem tanto depósitos (positivos) quanto saques (negativos).
Valor absoluto é o critério para filtrar, então tanto 300 (depósito) quanto -150 (saque) serão considerados, já que ambos têm módulo maior que 100.

Entrada
Uma lista de valores representando as transações bancárias (ex.: [100, -50, 300, -150]).
Um valor limite (inteiro ou decimal) fornecido pelo usuário.

Saída
Uma nova lista com as transações que ultrapassam o limite, no formato: "Transações: [X, Y, Z]"""


def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    for transacao in transacoes:
        if transacao > limite or transacao < -100:
            transacoes_filtradas.append(transacao)

    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
print(limite) 
limite = float(limite.strip())
print(limite) 

transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")