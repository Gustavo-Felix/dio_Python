''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    def __init__(self, titular: str, saldo: int = 0):
        self._titular = titular
        self._saldo = saldo
        self.operacao: list = []


    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
    def Depositar(self, valor: int):
        if not valor > 0:
            print('Valor inválido')
        
        self._saldo += valor

        self.operacao.append(f'+{valor}')

    # TODO: Implemente o método para realizar um saque:
    def Saque(self, valor: int):
        # TODO: Verifique se há saldo suficiente para o saque
        valorFiltrado = int(-valor)
        if valorFiltrado < self._saldo:
            # TODO: Subtraia o valor do saldo (valor já é negativo)
            self._saldo -= valorFiltrado
            # TODO: Registre a operação e retorne a  mensagem de saque negado
            self.operacao.append(f'{valor}')
        else:
            self.operacao.append("Saque não permitido")
        
    def Extrato(self):
        operacoes = ', '.join(self.operacao)
        print(f'Operações: {operacoes}; Saldo: {self._saldo}')
        
            
nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.Depositar(valor) 
    elif valor == 0:
        conta._saldo += valor
        conta.operacao += f'{valor}'
    else:
        conta.Saque(valor)  

conta.Extrato()