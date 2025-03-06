import os 
#Para checar se o arquivo existe
print(os.path.exists('arquivo')) #True or False
#Para checar se diretorios existem segue a mesma sintaxe

#Para criar arquivo utilizando with
with open('teste.txt', 'w') as arquivo:
    pass

os.mkdir('diretorio') #ou caminho do diretorio e novo diretorio. neste caso é criado um relativo
os.mkdir('c:\\user\\diretorio') #para criar absoluto

os.makedirs('teste/teste/teste') #Multi-diretorios 

os.rename('nome antigo', 'nomeatual') #Serve para renomear arquivos e diretórios

os.remove('teste.txt') #Exclui arquivos em definitivo, nao existe uma especie de "lixeira".

os.rmdir('diretorio') #Exclui diretorios mas apenas se estiverem vazios