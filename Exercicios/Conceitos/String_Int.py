#String
#Manipulacao de conteudo
str.upper() #Converte a string para maisculo
str.lower() #Converte a string para minuscilo
str.title() #Converte a primeira letra de cada palavra para maisuclo
str.swapcase() #Inverte maiscula e minuscula

#Verificaçao de conteudo
str.isalpha() # Retorna True se a string contém apenas letras.
str.isdigit() # Retorna True se a string contém apenas números.
str.isalnum() # Retorna True se a string contém apenas letras e números.
str.isspace() # Retorna True se a string contém apenas espaços em branco.
str.islower() # Retorna True se todos os caracteres forem minúsculos.
str.isupper() # Retorna True se todos os caracteres forem maiúsculos.

#Substituicao e formatacao
str.replace('old', 'new') #Substitui o antigo pelo novo
str.strip() #Remove os espaços no inicio e ao fim da palavra também existe a varicao de lstrip(esquerda) e rstrip(direita)

#Divisao
str.split() #Separa a string com base no delimitador passado
str.partition() #Separa a string em 3, antes, o delimitador passado e depois
str.join() #Junta os elementos de um iterável em uma string, separados pelo delimitador.

#Pesquisa
str.find() #Retorna o índice da primeira ocorrência de substring, ou -1 se não encontrado.
str.index() #Igual a find, mas lança uma exceção se não encontrar.
str.count() #Conta o número de vezes que substring aparece na string.

#----------------------------------------------------
#Int
#Operacoes matematicas
abs() #Retorna o valor absoluto
pow() #Passa-se dois argumentos e eleva o primeito a potencia do segundo

#Ordenacao
max() #Retorna o maior valor
min() #Retorna o menor valor

#Biblioteca Math
math.floor(4.7) #Arredonda para baixo #type: ignore
math.ceil(4.3) #Arredonda para cima  #type: ignore
random.randint(1, 10) #Gera um numero aleatorio dentro do range passado #type: ignore
