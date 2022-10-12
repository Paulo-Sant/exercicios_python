"""
RESOLVIDO!!!

Classe Retangulo:

Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa
que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as
medidas e calcular a quantidade de
pisos e de rodapés necessárias para o loca

---------------------------------------------
class Retangulo:
    def __init__(self, comprimento, largura):
        self.setcomprimento(comprimento)
        self.setlargura(largura)

    def setcomprimento(self, comprimento):
        self.comprimento = comprimento

    def setlargura(self, largura):
        self.largura = largura

    def getcomprimento(self):
        return self.comprimento

    def getlargura(self):
        return self.largura

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return (2 * self.comprimento) + (2 * self.largura)


compr = float(input('Informe o Valor do Comprimento: '))
larg = float(input('Informe o Valor da Largura: '))

retang = Retangulo(compr, larg)
print(f'A área é: {retang.area()}')
print(f'O perímetro é: {retang.perimetro()}')

"""

