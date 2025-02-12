# É reponsavel por arredondar numeros. podendo passar quantidade de casas necessárias

print(round(3.15))
print(round(3.78866886, 2)) 

lista = []
for i in range(3):
    numero = float(input(f'Me passe tres numeros racionais {i+1}/3: '))
    lista.append(numero)

lista_arredondada = [round(num, 2)for num in lista]
print(f'Aqui está a lista arredondada: {lista_arredondada}')