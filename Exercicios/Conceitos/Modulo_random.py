#Modulos nada mais sao do que os arquivos python 
#random -> possui funcoes para gerar numeros pseudo-aleatorios

from random import random #Gera um numero aleatorio real no intervalo de 0 : 1
from random import uniform #gera um numero aleatorio real no intervalo selecionado
from random import randint #Gera um numero aleatorio inteiro no interalo selecionado
from random import choice #Escolhe um elemento presente do parametro passado (lista, string, etc)
from random import shuffle #Embaralha os elementos (lista)

for i in range(5):
    print(random())

for i in range(5):
    print(uniform(10, 14)) #14 nao incluso

for i in range(5):
    print(randint(1,13), end=', ')

moeda = ['cara', 'coroa']
print(choice(moeda))

baralho = ['K', 'Q', 'J', 'A']
print(baralho)
shuffle(baralho)
print(baralho)
