# Cria um iteravel que agrega cada elemento do grupo com o do outro grupo, sempre respeitando a posicao original dos elementos em seus respectivos grupos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7, 8] #Neste caso ele ignora o restante (7 e 8) pois o resto das listas tem apenas 3 elementos
lista3 = ['a', 'b', 'c']

exemplo = zip(lista1, lista2, lista3)

print(list(exemplo))

#Exemplo 2
prova1 = [89, 90, 86]
prova2 = [79, 80, 65]
alunos = ['Pedro', 'Maria', 'Jose']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)