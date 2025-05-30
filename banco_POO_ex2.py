''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'{self.titular}: R$ {self.saldo}'

#TODO: Implemente a classe SistemaBancario:
class SistemaBancario(ContaBancaria):
    # TODO: Inicialize a lista de contas:
    def __init__(self, contas:list = []):
        self.contas = contas

    # TODO: Crie uma nova conta e adicione à lista de contas:
    def criar_conta(self, titular, saldo):
        contacriada = ContaBancaria(titular, saldo)
        self.contas.append(contacriada)
        return contacriada

    # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    def listar_contas(self):
        for i, conta in enumerate(self.contas):
            if i < len(self.contas) - 1:
                print(conta, end=", ")  # Adiciona vírgula para todos, exceto o último
            else:
                print(conta)

#TODO: Crie uma instância de SistemaBancario:

sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()