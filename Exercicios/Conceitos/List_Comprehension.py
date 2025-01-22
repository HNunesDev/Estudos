"""
List_Comprehension é uma funcionalidade do python onde é possivel fazer uma lista a partir de um conjunto de iteraveis
sintaxe = [] 
"""

lista1 = [1,2,3,4,5]

lista2 = [n * 10 for n in lista1]
print(lista1)
print(lista2)

nome = 'henrique'
nome_upper = [nome.title()]
print(nome_upper)

#É posssivel também utilizar operador lógico em sua estrutura
numeros = [1,2,3,4,5,6]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(pares)
print(impares)

teste = [numero * 2 if numero %2 == 0 else numero/2 for numero in numeros]
print(teste)
