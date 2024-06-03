import time

#Encontrar o maior valor na lista - exemplo 1
list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = list[0] #recebeu o numero 17

for i in range(1, len(list)):
    if list[i] > maior_numero:
        maior_numero = list[i]
print("O maior número da lista é:", maior_numero)        





#exemplo2
my_list = [17, 3, 11, 5, 1, 9, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Maior valor 2:", maior)




 #Exemplo3
ultima_lista = my_list[:]
mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
     mel = i
print("Maior valor 3:", mel)


#Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maça", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("Elemento encontrado no índice:", i)
else:
        print("NÃO ENCONTRADO!!!")


#Conferidor de aposta em loteria
sorteados = [5, 11, 9, 42, 3, 49]
sorteados = [3, 7, 11, 42, 34, 49]
acerto =0

for numero in sorteados:
    if numero in sorteados:
        acerto += 1

print(acerto)


#Remoção de npumeros repetidos em uma lista
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original:", lista)


#Lista de apoio
vistos = []


#Interar pela lista original de trás para frente
for i in range(len(lista ) - 1, - 1, - 1):
    #se o número ja está na lista "vistos", remove-lo da lista original
    if lista[i] in vistos :
        del lista[i]
    else:
        #Caso contrário adicionar á lista "visto"
        vistos.append(lista[i])

        print("lista modificada", lista)

    #Listas avançadas
    #2D - listas aninhadas bidimensionais
    tabela = [[" :( ", " :) ", " :| ", " ;-; "],
              [" ;-; ", " :| ", " :) ", " :( "],
              [" :| ", " :) ", " ;-; ", " :( "]]
               
print(tabela[0][3])
print(tabela)



#3D - Matriz Tridimensional
cubo = [[ [":(", "y", "z" ],
        [":)","y","z" ],
        [":|","y","z" ]],
        
        [ ["amor","ódio","caridade" ],
        ["paz","esperança","férias" ],
        ["tina","prior","pp" ]],

        [ ["restinga","patrocinio","rifania" ],
        ["amazonense","fluminence","santos" ],
        ["pizza","lasanha","pastel" ]]]

print(cubo)
print(cubo[1])
print(cubo[1][0])
print(cubo[1][0][2])

time.sleep(3)
