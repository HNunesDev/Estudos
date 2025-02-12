# Passa quantidade de elemento em uma lista, tupla, dicionario e quando passado para um string retorna a quantidade de caracter

lista = [1,2,3,4,5,6]
print(len([1,2,3,4,5,6]))
print(len('Olá'))

#ex
for i in range(len(lista)):
    print(f'olá essa já é a {i+1} que escrevo')
    i += 1
