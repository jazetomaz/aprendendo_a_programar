from argparse import BooleanOptionalAction


fruit = 'banana'
letra = input('Informe a letra a ser buscada: ')
if letra in fruit:
    print('Done!')
else:
    print('Não encontrado')
