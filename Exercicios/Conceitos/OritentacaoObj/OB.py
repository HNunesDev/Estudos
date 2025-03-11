"""
É um dos paradigmas mais utilizados - paradigmas sao formas ou metodologias de se programas
Python suporta os 3 paradigmas - Orientada a objetos, estruturada e funcional

Objeto da programas orientada a objeto é mapear objetos do mundo real para modelos computacionais 

Método = funcao - Unica diferença é que o metodo pertence a uma classe
Construtor -> Método especial utilizado para criar objetos
Objeto -> Instancia da classe
"""
#Classe -------------------------------------------------------------------------------------------------
"""
Classe é a representacao do objeto real no modelo computacional
Quando se cria uma classe está criando um novo tipo para as variaveis
Utiliza-se sempre letra maiscula pra nome de classes e se necessario camelcase 
Nao se deve utilizar acentos.
Toda variavel criada a partir da classe leva o nome de instancia
"""
#Exemplo
class Lampada:
    pass
lamp = Lampada()
print(type(lamp))

#Atributos -------------------------------------------------------------------------------------------------
"""
Atributos sao caracteristicas do objeto
Em Python todo atributo de uma classe é público, caso queira delcarar o atributo como privado é necessario utilizar o __antes do nome do atributo, porém é possivel fazer acesso ao atributo mesmo assim
Existem tres tipos de atributos: 
    -Atributos de Instancia
        -São atributos delcarados dentro do método do construtor
    -Atributos de Classe
        -São atributos declarados dentro do classe, e tera um valor "universal" para todos as instancias da classe
        -São utilizados também, pois economizam espaco de memoria
    -Atributos Dinamicos
        -São atritos de instancia que podem ser criados em tempo de execucao
        -O atributo será exclusivo da instancia que o criou
"""
#Exemplo publico
class Cachorro:
    animal = True #Exemplo de atributo de classe
    def __init__(self, cor, tamanho, sexo):
        self.cor = cor
        self.tamanho = tamanho
        self.sexo = sexo

caramelo = Cachorro('Caramelo', 'Grande', 'Macho')
caramelo.peso = '23kg'

print(caramelo.peso) #Exemplo de atributo dinamico, o peso nao existe na classe mas crio em tempo de execucao e mesmo assim ele recebe o valor para essa instancia
print(caramelo.__dict__) #Gera um dicionario com todos atributos e seus respectivos valores
del caramelo.peso #Serve para excluir um atributo
print(caramelo.__dict__)

from passlib.hash import pbkdf2_sha256 as cryp #Biblioteca responsalve por encriptar senha round quantidade de vezes que embralha e salt quantos carcteres sera adicionado a senha
#Exemplo privado 
class Acesso:
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = cryp.hash(senha, round = 200000, salt_size = 16)

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

#Métodos -------------------------------------------------------------------------------------------------
"""
São como funcoes -> Representam os comportamentos do objeto, ou seja, as acoes que esse objeto pode realizar no codigo
-Metodo de instancia
    -Necessita da instancia do objeto para poder fazer acesso a ele
-Metodo de classe

O método __init__ é um método especial chamado de construtor. Sua funcao é construir o objeto a partir da classe
"""
class Produto:

    def __init__(self, produto, valor):
        self.__produto = produto
        self.__valor = valor
        

    def total(self, quantidade): #Isso aqui é o metodo de de instrancia, pois é precos passar a quantidade para saber quanto vai ser pago no produto
        """Calcula o total a ser pago com base no valor e quantidade"""
        return self.__valor * quantidade
    
pc = Produto("Computador", 3500)
print(pc.total(2))

