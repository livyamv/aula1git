import time

numeros = [111, 7, 2, 1]

#imprime a quantidade de numeros da lista
print(len(numeros))

#adiciona um numero á lista
numeros.append(52)
print(len(numeros))

#imprime a lista
print(numeros)


#insere um valor na lista de acordo com o lugar que voce escolheu
numeros.insert(0, 222)

print(len(numeros))
print(numeros)

numeros.insert(-1, 12)
print(numeros)

numeros.insert(1, 18)
print(numeros)

numeros.insert(-2, 20)
print(numeros)


time.sleep(3)
