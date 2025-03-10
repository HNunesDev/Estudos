'''
Entendendo iterator e itrables

Iterator -> É um objeto que pode ser iterado . É um objeto que retorna um dado, sendo um elemento por vez quando a funcao next() é chamada

Iterable -> É um objeto que retorna um iterator quando a funcao iter() for chamada
'''

#EX
nome = 'Henrique' #É um iterable mas nao um iterator
#Caso puxe mais iteraveis do que realmente tem, da erro StopIteration
it1 = iter(nome)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

#Basicamente quando pedimos o codigo abaixo é o que o python tranforma em iterator e chama a funcao next ate a quantidade exata
for letra in nome:
    print(f'{letra}')