"""
RESOLVIDO!!!

5. Classe Conta Corrente:
Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.


class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0.0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        self.nome_correntista = input('Informe um novo nome: ')
        return self.nome_correntista

    def deposito(self):
        self.saldo = float(input('Digite um Valor para depósito: '))
        return self.saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor


a = ContaCorrente(123456, 'Paulo Santana', 100.0)
print(vars(a))
a.saque(30)
print(vars(a))
"""
