from abc import ABC, abstractmethod
from datetime import datetime, date
import time
import os

class Cliente:

    def __init__(self, endereco: str):
        self._endereco = endereco
        self.contas: list = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class Conta:

    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, numero: int, cliente: Cliente):
        return cls(numero, cliente)

    def sacar(self, valor: float):
        if valor <= self.saldo:
            self._saldo -= valor
            print("Saque feito com sucesso!")
        else:
            print("Valor inválido!")
    
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print("Depósito feito com sucesso!")
        else:
            print("Valor inválido!")
    
class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            Conta Corrente:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class PessoaFisica(Cliente):

    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta: Conta):
        pass
      
class Historico:

    def __init__(self):
        self._historico = []

    @property
    def historico(self):
        return self._historico
    
    def adicionar_transacao(self, transacao):
        self._historico.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y"),
            }
        )

class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        conta.sacar(self._valor)
        conta.historico.adicionar_transacao(self)

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        conta.depositar(self._valor)
        conta.historico.adicionar_transacao(self)

def menu():

    time.sleep(2)
    os.system('cls')

    menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Contas
[6] Novo Cliente
[7] Sair
=> """
    return int(input(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf] # Procura em cada cliente se o campo 'cpf' é igual ao cpf digitado.
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("O Cliente não possui conta.")
        return

    return cliente.contas[0]

def depositar(clientes):
    cpf = str(input('Digite seu cpf: '))
    cliente: Cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return
    
    valor = float(input('Digite o valor que deseja depositar: '))
    trasicao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    cliente.realizar_transacao(conta, trasicao)

def sacar(clientes):
    cpf = str(input('Digite seu cpf: '))
    cliente: Cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return
    
    valor = float(input('Digite o valor que deseja sacar: '))
    trasicao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)

    cliente.realizar_transacao(conta, trasicao)

def exibir_extrato(clientes):
    cpf = str(input('Digite seu cpf: '))
    cliente: Cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return
    
    conta: Conta = recuperar_conta_cliente(cliente)

    transacoes = conta.historico.historico

    extrato = ""
    if not transacoes:
        extrato = "Não foi feito nada."
    else:
        for transacao in transacoes:
            extrato += f'{transacao['tipo']} - {transacao['valor']}\n'

    print(extrato)
    print(f"\nSaldo: R$ {conta.saldo:.2f}")

def criar_cliente(clientes):
    cpf = input("Digite seu cpf: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe cliente com esse cpf!")
        return

    nome = input("Digite o seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("Cliente criado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o cpf do cliente: ")
    cliente: Cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = ContaCorrente.nova_conta(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print(f'\n{conta}')

def main():
    
    clientes = []
    contas = []

    while True:

        opc = int(menu())

        if opc == 1:
            depositar(clientes)

        elif opc == 2:
            sacar(clientes)

        elif opc == 3:
            exibir_extrato(clientes)

        elif opc == 4:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        
        elif opc == 5:
            listar_contas(contas)

        elif opc == 6:
            criar_cliente(clientes)

        elif opc == 7:
            break

        else:
            print("Opção inválida.")

main()