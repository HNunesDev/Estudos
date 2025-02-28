#Para abrir arquivos para leitura utilizamos a funcao open() e o parametro orbigatorio é o caminho para o arquivo
#EX

arquivo = open('teste.txt') # Retorna um tipo um _io.TextIOWrapper
#Dessa maneira apenas abre o arquivo, caso queira ler é preciso utilizar a funcao read
print(arquivo.read()) #Assim apareceria o conteudo do arquivo txt no console


