"""
# RESOLVIDO - Exercício 1: Faça um Programa que possua um vetor
denominado A, que armazene 6 números inteiros.
o programa deve executar os seguintes Passos:

(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.

lista = [1, 0, 5, -2, -5, -7]

(b) Armazene em uma variável (simples)
a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.

lista = [1, 0, 5, -2, -5, -7]
soma = sum(lista[0:3])

print(soma)

(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.

lista = [1, 0, 5, -2, -5, -7]
lista[4] = 100
print(lista[4])

(d) Mostre na tela cada valor do vetor A, um em cada linha.

1 - exemplo com list comprehension

lista = [1, 0, 5, -2, -5, -7]

[print(numero) for numero in lista]
************************************
2 - exemplo com laço for

lista = [1, 0, 5, -2, -5, -7]

for numero in lista:
    print(numero)
-----------------------------

# RESOLVIDO - Exercício 2: Crie um programa que lê
6 valores inteiros e, em seguida, mostre na tela os valores lidos.

lista = []

for numero in range(6):
    numeros = int(input('Digite um Numero: '))
    lista.append(numeros)
print(lista)
-----------------------------

# RESOLVIDO - Exercício 3: Ler um conjunto de números reais,
armazenando-o em um vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor.
os conjuntos tem 10 elementos cada.
imprimir todos os conjuntos.

lista = []
quadrado = []

for numero in range(10):
    numeros = float(input('Digite um Numero: '))
    lista.append(numeros)

quadrado = list(map(lambda x: x**2, lista))

print(lista)
print(quadrado.__str__())
---------------------------------------------------------

# RESOLVIDO - Exercício 4: Faça um programa que leia um vetor de 8 posições , em seguida, leia também dois valores X e Y
quaisquer correspondentes a duas posições no vetor.
Ao Final Seu Programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.

vetor = []

for numero in range(8):
    numeros = int(input('Digite um Numero: '))
    vetor.append(numeros)

x = vetor[3]
y = vetor[2]

soma = x + y

print(soma)
----------------------------------------

# RESOLVIDO - Exercício 5: Leia um vetor de 10 posições.
Contar e escrever quantos valores pares ele possui.

vetor = []
contador = 0

for numero in range(10):
    numeros = int(input('Digite um Valor: '))
    vetor.append(numeros)

    if numeros % 2 == 0:
        contador = contador + 1

print(vetor)
print(f'Seu Vetor possui {contador} valores pares')

-------------------------------------------

#Parte Do Exercício 5: Achei coveniente guardar este código, fiz por acidente,
basicamente ele me traz os números pares através dos índices.

vetor = []
contador = []

for numero in range(4):
    numeros = int(input('Digite um Valor: '))
    vetor.append(numeros)

    if numeros.__index__() % 2 == 0:
        contador.append(numeros)

print(contador)
----------------------------------------------

# NÃO RESOLVIDO - Exercício 6: Faça um programa que receba do usuário um vetor com 10 posições.
Em seguida deverá ser impresso o maior e o menor elemento do vetor.


"""


