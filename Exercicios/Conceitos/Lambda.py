"""
Lambda são funcoes sem nome (funcoes anonimas), sao constantemente utilizadas para ordenacao e filtragem de dados
sintaxe -> lambda parametros: retorno da funcao
"""
#Maneira nao convencionou de se utilizar lambda
lambda x: x**2
cal = lambda x: x**2
print(cal(2))
print(cal(3))

#Maneira mais comumente utilizada
#Ordenando os autores de acordo com sobrenome
autores = ['Machado de Assis', 'Clarice Lispector', 'Paulo Freire', 'Jorge Owell', 'Anne Frank', 'Nicollas Maquiavel']
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

#Outro exemplo
#Ordenando por valor absoluto e pegando apenas os positivos
numeros = [3, -1, -4, 2, 7, -9, 0, -5]
numeros.sort(key = lambda x: abs(x))
print(numeros)

positivos = list(filter(lambda x: x >0, numeros))
print(positivos)
negativos = list(filter(lambda x: x <0, numeros))
print(negativos)
