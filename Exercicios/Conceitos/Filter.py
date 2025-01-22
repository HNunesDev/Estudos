""""
Serve pra filtrar os dados, retorna um iteravel. Fica na memória apenas até a primeira utilizacao
Sintaxe -> fiter(funcao, iteravel)
"""

#Ex 
import statistics as str
dados = 1,2,3,4,5,6,7,8,9

filtro = filter(lambda x: x>str.mean(dados), dados)
print(list(filtro))

#EX2 utilizando filter e map - filtrando por nome maior que 6 letras

nomes = ['Vitória', 'Vanessa', 'Joana','Valentina','Jeromeia']
res = map(lambda nome: nome, filter(lambda nome: len(nome) > 6, nomes))
print(list(res))