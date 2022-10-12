"""
RESOLVIDO!!!

Faça  um  programa  que  simule  um  televisor  criando-o  como  um  objeto.
O  usuário  deve  ser  capaz  de  informar  o  número  do  canal  e  aumentar  ou  diminuir  o  volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
--------------------------------------------------------------------------------------------------------

class Tv:
    def __init__(self, canais, volume):
        self.canais = canais
        self.volume = volume

    def aumenta_volume(self):
        if self.volume >= 0:
            self.volume += 1

    def diminui_volume(self):
        if self.volume <= 100:
            self.volume -= 1

    def muda_canal(self):
        if self.canais >= 0:
            self.canais += 1


a = Tv(3, 5)
print(vars(a))
a.muda_canal()
print(vars(a))
a.aumenta_volume()
print(vars(a))
"""
