
"""
#Exercício 1 - Criar um Algoritmo que mostre os 5 primeiros múltiplos de qualquer número

numero = int(input("Insira um Número: "))
cont = 1
while cont <= 5:
    print(numero * cont)
    cont = cont + 1
-------------------------------------------------
#Exercício 2 - Criar um Laço que vai de 1 a 100 nas duas estruturas (for e while)
for i in range(1, 101, 1):
    print(i)

n = 1
while n < 101:
    print(n)
    n = n + 1
------------------------------------------------
#Exercício 3 - Criar um laço onde realiza uma contagem regressiva de 10 a 0 e ao final dizer a palavra fim
numero = 10
while numero >= 0:
    print(numero)
    numero = numero - 1
print('Fim')
------------------------------------------------
#Exercício 4 - Inicialize uma variável com 0, e incremente-a de 1000 em 1000 até chegar 100000
#Encontrei duas formas de resolver esse problema.

*primeira forma*

cont = 0
for cont in range(0, 100001, 1000):
    print(cont)
    cont = cont + 1

*segunda forma*
*Deste modo não iria valer porque não incrementa os valores de 1000 em 1000, mas chega ao valor final.*

cont = 0
for cont in range(0, 100001):
    print(cont)
    cont = cont + 1000
--------------------------------------------------
Exercício 5 - faça um programa que peça ao usuário 10 valores e some-os

n = 1
soma = 0

while n <= 10:
    x = int(input('Digite um Número: '))
    soma = soma + x
    n = n + 1
print(f'Total: {soma}')
--------------------------------------------
Exercício 6 - Fatorial de um número

numero = int(input('Digite Um Número: '))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1
print(f'Resultado: {fatorial}')
------------------------------------
#fatorial 2

numero = int(input('Fatorial de '))

contador = 1
for n in range(1, numero+1):
    contador *= n
print(contador)
------------------------------------
Exercício 7 - soma idades

idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total += idade

print(total)
-------------------------------------
Exercício 8 - soma maiores e menores - faça um algoritmo que receba 10 números e imprima o maior e o menor entre eles

lista = []

for numeros in range(1, 6):
    numero = int(input('Digite o numero: '))
    lista += [numero]
print(f'O maior peso foi {max(lista)}')
print(f'O menor peso foi {min(lista)}')
--------------------------------------
Exercício 9 - faça um programa que leia 10 inteiros e imprima sua média

import statistics

lista = []

for numeros in range(1, 5):
    numero = int(input('Digite um numero: '))
    lista += [numero]
print(f'Média: {statistics.mean(lista)}')
---------------------------------------
#outra forma
media = 0

for numeros in range(1, 5):
    numero = int(input('Digite um Número: '))
    media += numero

print(media/4)
---------------------------------------
Exercício 10 - leia um numero par e imprima todos os numeros pares de 0 até n (Ordem Crescente)

numero = int(input('Digite um Número: '))

for n in range(numero):
    if n % 2 == 0:
        print(n+2)
----------------------------------------
Exercício 11 - leia um numero par e imprima todos os numeros pares de 0 até n (Ordem Decrescente)

numero = int(input('Digite um Número: '))

for n in range(numero, -1, -2):
    if n % 2 == 0:
        print(n)
-----------------------------------------
Exercício 12 - leia um número inteiro positivo n e imprima todos os numeros naturais de 0 até n (Ordem Crescente)

numero = int(input('Digite um Número: '))

for numeros in range(numero):
    print(numeros + 1)
------------------------------------------
Exercício 13 - leia um número inteiro positivo n e imprima todos os numeros naturais de 0 até n (Ordem Decrescente)

numero = int(input('Digite um Número: '))

for numeros in range(numero, -1, -1):
    print(numeros)
------------------------------------------
Exercício 14 - leia um numero ímpar e imprima todos os numeros de 0 até n (Ordem Decrescente)

numero = int(input('Digite um Número: '))

for n in range(numero, -1, -2): #Fiz o Teste com a parte iterável (-2), tanto faz se for -1 também
    if n % 2 == 1:
        print(n)

------------------------------------------
Exercício 15 - leia um numero ímpar e imprima todos os numeros de 0 até n (Ordem Crescente)

numero = int(input('Digite um Número: '))

for n in range(numero):
    if n % 2 == 1:
        print(n)
------------------------------------------
Exercício 16 - Faça um programa que calcule a soma dos numeros pares e a multiplicação dos números ímpares

soma = 0
multiplicacao = 1

for c in range(1, 7):
    numero = int(input(f'Digite o {c} numero: '))
    if numero % 2 == 0:
        soma += numero

    if numero % 2 == 1:
        multiplicacao = multiplicacao * numero


print(f'A Soma Total dos pares foi de {soma}')
print(f'A Multiplicação dos ímpares foi de {multiplicacao}')

"""
