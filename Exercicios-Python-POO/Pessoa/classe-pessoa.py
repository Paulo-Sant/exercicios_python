"""
RESOLVIDO!!!

Classe Pessoa:
Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm.

--------------------------------------------------
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos

        if self.idade < 21:
            self.altura = self.altura + 0.5
        else:
            print('Não Cresce Mais')

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


a = Pessoa('Paulo', 26, 72, 170)
print(vars(a))
a.engordar(6)
print(vars(a))
a.emagrecer(6)
print(vars(a))
a.crescer(2)
print(vars(a))
a.envelhecer(3)
print(vars(a))


"""
