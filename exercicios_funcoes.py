"""
# RESOLVIDO - Exercício 1: Crie uma função que exibe uma saudação com os parâmetros saudação e nome

forma 1:
def saudacao(saud, nome):
    return f'{saud}, {nome}'


print(saudacao('Saudações', 'Paulo'))

forma 2:
def saudacao(saud, nome):
    print(f'{saud} {nome}')


saudacao(Olá, Paulo)
------------------------------------

# RESOLVIDO - Exercício 2: Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

def soma(x, y, z):
    return x + y + z


print(soma(7, 3, 5))
------------------------------------

# RESOLVIDO - Exercício 3: Crie uma Função que receba 2 Números.
O primeiro é um valor e o segundo um percentual, ex(10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.

def porcento(valor, porcentagem):
    return valor + (valor * porcentagem / 100)


print(f'Porcentagem {porcento(15, 100)}')
-------------------------------------

# RESOLVIDO - Exercício 4: Crie uma função  que 
recebe como parâmetro um número inteiro e devolve o seu dobro.

def dobro(x):
    return x * 2

print(dobro(4))
-------------------------------------

# RESOLVIDO - Exercício 5: Faça uma função que receba a data atual (dia, mês e ano em inteiro)
e exiba na tela no formato textual por extenso.

import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')


def retorna_data_extenso(data_string):
    try:
        datetime.strptime(data_string, '%d/%m/%Y')
    except ValueError:
        print("Formato de Data inválido, deve ser DD/MM/AAAA")
        return None
    else:
        data_datetime = datetime.strptime(data_string, '%d/%m/%Y')
        # return datetime.strftime(data_datetime, '%d de %B de %Y')

        dia = datetime.strftime(data_datetime, '%d')
        mes = datetime.strftime(data_datetime, '%B')
        ano = datetime.strftime(data_datetime, '%Y')
        return dia + " de " + mes[0].upper() + mes[1:] + " de " + ano
        # return dia + " de " + mes.capitalize() + " de " + ano


data = input('Digite uma data no formato DD/MM/AAAA: ')
data_extenso = retorna_data_extenso(data)

if data_extenso is not None:
    print(data_extenso)
---------------------------------------------

# RESOLVIDO - Exercício 6: Faça uma função para verificar se um número é positivo ou negativo,
sendo que o valor de retorno será de 1 se positivo, -1 se negativo e 0 se for igual a 0.

def verifica_numero():
    numero = int(input('Digite um Número: '))
    if numero == 0:
        return '0'
    if numero < 0:
        return '-1'
    if numero > 0:
        return '1'


print(verifica_numero())
----------------------------------------------

# RESOLVIDO - Exercício 7: Faça uma função para verificar se um número é um quadrado perfeito.
um quadrado perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de outro número.

def quadrado_perfeito():
    x = int(input('Digite um Número: '))

    raiz_de_x = int(x ** 0.5)

    if raiz_de_x ** 2 == x:
        return f'O número {x} é um quadrado perfeito'
    else:
        return f'O número {x} não é um quadrado perfeito'


print(quadrado_perfeito())
----------------------------------------------

# RESOLVIDO - Exercício 8: Faça uma função que receba
uma temperatura em graus celsius e retorne-a convertida em graus fahrenheit.

def conversor_de_temperatura():
    celsius = int(input('Digite a Temperatura: '))

    fahrenheit = celsius * (9.0/5.0) + 32

    return f'Valor Convertido para fahrenheit {fahrenheit}'


print(conversor_de_temperatura())
----------------------------------------------

# RESOLVIDO - Exercício 9: Sejam a e b os catetos de um triângulo,
onde a hipotenusa é obtida pela equação: hipotenusa = raizQ a ** 2  +  b ** 2.
Faça uma Função que receba os valores de a e b e calcule o valor da hipotenusa através da equação.

def valor_hipotenusa():
    a = int(input('Digite um Número: '))
    b = int(input('Digite outro Número: '))

    hipotenusa = (a ** 2 + b ** 2) ** 0.5

    return f'O valor da Hipotenusa é {hipotenusa:.2f}'


print(valor_hipotenusa())
-----------------------------------------------

# RESOLVIDO - Exercício 10: -> Crie uma função que encontra o primeiro duplicado considerando o segundo
#     número como a duplicação. Retorne a duplicação considerada.
#         Requisitos:
#             A ordem do número duplicado é considerada a partir da segunda
#             ocorrência do número, ou seja, o número duplicado em si.
#             Exemplo:
#                 [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#                 [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#             Se não encontrar duplicados na lista, retorne -1

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def encontra_duplicado(lista_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_duplicado(lista_de_inteiros))
--------------------------------------------------------------------

"""
