""""
All retorna TRUE se TODOS os valores dentro de um iteravel forem True
"""
#Ex01 all

dados = [0,1,2,3,4]
print(all(dados)) #Retornará false pois o 0 é F
dados = [1,2,3,4]
print(all(dados)) #Ja aqui nao

print(all(letra for letra in 'aei2' if letra in 'abcdefghijklmnoopqrstuvwxyz')) #-> neste caso se tiver qualquer letra ele ja retorna true

"""
Já o Any se qualquer um dos elementos do iteravel for T ele retornara True, porém iteravel VAZIO é retornado False
"""

dados = [0,1,2,3,4]
print(any(dados)) #Como visto no exemplo anterior ele retorna T