'''
#Primeiro Exercicio
def dobro(numero):
    return numero * 2

pt1 = dobro(2)
pt2 = dobro(3)
pt3 = dobro(90)

print(f'primeiro {pt1}, segundo {pt2} e terceiro {pt3}')

#Segundo Exercicio

def data_extenso(data : str) -> None:
    data = data.split('/')
    dia : int = int(data[0])
    mes : int = int(data[1])
    ano : int = int(data[2])
    if mes == 1:
        mes_extenso = 'Janeiro'
    elif mes == 2:
        mes_extenso = 'Fevereiro'
    elif mes == 3:
        mes_extenso = 'Março'
    elif mes == 4:
        mes_extenso = 'Abril'
    elif mes == 5:
        mes_extenso = 'Maio'
    elif mes == 6:
        mes_extenso = 'Junho'
    elif mes == 7:
        mes_extenso = 'Julho'
    elif mes == 8:
        mes_extenso = 'Agosto'
    elif mes == 9:
        mes_extenso = 'Setembro'
    elif mes == 10:
        mes_extenso = 'Outubro'
    elif mes == 11:
        mes_extenso = 'Novembro'
    elif mes == 12:
        mes_extenso = 'Dezembro'
    else:
        mes_extenso = 'Mês inexistente'
    print(f'{dia} de {mes_extenso} de {ano}')

teste = data_extenso('01/01/2024')
teste2 = data_extenso('13/03/2002')
teste3= data_extenso('19/06/2018')
'''
#Terceiro Exercicio
def maior(lista_num : list[int]):
    return max(lista_num)

lista= [0,1,2,3,4,5,6,7,8,9,10,99]
print(f'O maior valor da {lista}, é {maior(lista)}')
