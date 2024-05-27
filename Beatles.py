import time

#lista vazia
beatles = []

#adicionando os membros da banda à lista
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('Geroge Harrison')

print(beatles)
print()

# solicitar que o usuário digite os seguintes membros da banda:
# Stu Sutcliffe e Pete best para serem adicionados á lista
for i in range(2):
    if i == 1:
        print()
        digitado = str(input('Escreva "Stu Sutcliffe" para adicioná-lo à banda: '))
        beatles.append(digitado)
    else:
        digitado = str(input('Escreva "Pete Best" para adicioná-lo à banda:'))
        beatles.append(digitado)

print(beatles)
print()

#remover Stu Sutcliffe e Pete Best da lista
del(beatles[-1])
del(beatles[-1])


print(beatles)
print()

#adicionar Ringo ao primeiro da lista
beatles.insert(0, "Ringo Starr")

print(beatles)
print()

time.sleep(3)