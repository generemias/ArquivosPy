import random
n1 = str(input('primeiro'))
n2 = str(input('segundo'))
n3 = str(input('terceiro'))
n4 = str(input('quarto'))
lista =[n1,n2,n3,n4]
#bagunça a lista
random.shuffle(lista)
print('a ordem de da lista agora é {}'.format(lista))