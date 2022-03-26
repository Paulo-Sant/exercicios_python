numeros_strings = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
comp = [numeros_strings[i:i + 10] for i in range(0, len(numeros_strings), 10)]
lista = '.'.join(comp)
print(lista)
