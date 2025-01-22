"""
Reduce é raramente utilizado, normalmente se utiliz o loop for para resolver o problema
Mas basicamente ele aplica a funcao nos dois primeiros dados e guarda o valor, e a partir dai ele aplica a funcao com o valor guardado e utiliza o 3 dado, e assim por diante
É necessário import a funcao: from functools import reduce
Sintaxe -> reduce(funcao, iteravel)
"""
#Ex
from functools import reduce

dados = [1, 2, 3, 4, 5, 6]
teste = reduce(lambda x, y: x * y, dados)
print(teste)

#Essa seria a forma de se utilizar o loop for
res = 1
for i in dados:
    res = res*i
print(res)