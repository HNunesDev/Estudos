'''
Basicamnete matriz nas outras linguagens ou vetor
'''
matriz = [[1,2,3], [4,5,6], [7,8,9]]

print(matriz[0][1])

#Gerando matriz 3x3

#O primeiro for cria os valores dentro de cada lista e o segundo cria as listas
m3 = [[n for n in range(1,4)] for valor in range(1,4)]
print(m3)