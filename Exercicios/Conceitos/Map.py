"""
Map basicamente recebe um iteravel de entradas e passa pela funcao desejada. Fica na memória apenas até a primeira utilizacao
sintaxe -> x = map(funcao, iteravel)
"""
import math

def area(r):
    return math.pi * (r ** 2)

raios = [1,2,3,5.4,3.9,8.1,3.14,4,5]

teste = map(area, raios)
#Passa o tipo de saida que for necessário, neste caso, lista
print(list(teste))

#Neste caso ainda mais conciso e utilizando o conceito de lambda
teste2 = map(lambda x: math.pi * (x**2), raios)
print(tuple(teste2))

#Exemplo 2 - Convertendo Celcius em fahrenheit
cidade = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19)]
fahrenheit = map(lambda dado:(dado[0], (9/5) * dado[1] + 32), cidade)
print(list(fahrenheit))

#Exemplo parecido apenas para fixard
Animais = [(130, 'Vaca'), (86, 'Ovelha'), (19, 'Cao'), (5, 'Gato')]
peso = map(lambda lista: (lista[0]+ 7.8, lista[1]), Animais)
print(list(peso))
