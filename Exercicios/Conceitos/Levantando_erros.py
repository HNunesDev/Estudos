#Utiliza-se da palavra reservada "raise" para criar a mensagem de erro, passando o tipo do erro e seu texto
#EX raise TipoDoErro('texto')
#raise finaliza o código, nada além dele é executado

def calendario(dia, mes):
    dias = range(1, 32)
    if not isinstance(dia, int):
        raise TypeError('O dia precisa ser um numero inteiro')
    if not isinstance(mes, str):
        raise TypeError('O Mes precisa ser string')
    if dia not in dias:
        raise ValueError(f'O dia informado tem que estar entre {dias}')
    print(f'Hoje é dia {dia} de {mes}')


calendario(13, 'Março')