# Cria um iteravel que agrega cada elemento do grupo com o do outro grupo, sempre respeitando a posicao original dos elementos em seus respectivos grupos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7, 8] #Neste caso ele ignora o restante (7 e 8) pois o resto das listas tem apenas 3 elementos
lista3 = ['a', 'b', 'c']

exemplo = zip(lista1, lista2, lista3)

print(list(exemplo))