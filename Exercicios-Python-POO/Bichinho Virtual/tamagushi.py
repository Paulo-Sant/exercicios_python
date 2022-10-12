"""
RESOLVIDO!!!!
------------------------------------------------------

Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos:  Nome,  Fome,  Saúde  e  Idade
Métodos:  Alterar  Nome,  Fome,  Saúde  e  Idade;  Retornar  Nome,  Fome,  Saúde  e  Idade
Obs:  Existe  mais  uma  informação  que
devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome  e Saúde,
ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação
por que ela pode ser calculada a qualquer momento.
--------------------------------------------------------

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self):
        self.nome = input('Informe um Novo Nome: ')
        return self.nome

    def aumentar_fome(self):
        self.fome += 1
        return self.fome

    def diminui_fome(self):
        self.fome -= 1
        return self.fome

    def aumentar_saude(self):
        if self.saude == 10:
            print('Saúde no Máximo!')
        else:
            self.saude += 1
        return self.saude

    def diminuir_saude(self):
        if self.saude == 0:
            print(f'{a.nome} Morreu ;(')
        else:
            self.saude -= 1
        return self.saude

    def aniversario(self):
        self.idade += 1
        return self.idade

    def felicidade(self):
        if self.fome and self.saude >= 5:
            print(f'{a.nome} está Feliz!')
        else:
            print(f'{a.nome} está Triste!')

a = Tamagushi('Charizard', 6, 5, 1)
print(vars(a))
a.felicidade()
print(vars(a))

"""
