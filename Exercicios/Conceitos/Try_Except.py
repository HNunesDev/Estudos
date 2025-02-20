# É utilizado para tratar erro que podem surgir no código, previnindo que o programa pare de funcionar
'''
try:
    Execucao do problema
except:
    Como seguir a partir do problema
'''
#Ex 1

def pega_valor(dicionario, chave):
    try:
     return dicionario[chave]
    except KeyError:
       return None
    except TypeError:
       return None

dic = {'olá': '23'}
print(pega_valor(1,'olá'))

#EX 2
def divisao(a,b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('O valor precisa ser inteiro')
    except ZeroDivisionError:
        print('Impossivel realizar a divisao por 0')

num1 = input('Passe o primeiro valor: ')
num2 = input('Passe o segundo valor: ')
print(divisao(num1, num2))