"""
RESOLVIDO!!

Classe Quadrado: Crie uma classe que modele um quadrado:
a) Atributos: Tamanho do lado
b) Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado:
    def __init__(self, tamanho_do_lado=9):
        self.tamanho_do_lado = tamanho_do_lado

    def muda_valor_do_lado(self):
        self.tamanho_do_lado = int(input('Informe um Valor: '))
        return self.tamanho_do_lado

    def calcula_area(self):
        self.tamanho_do_lado *= self.tamanho_do_lado
        return self.tamanho_do_lado


a = Quadrado()
a.muda_valor_do_lado()

print(a.calcula_area())

"""
