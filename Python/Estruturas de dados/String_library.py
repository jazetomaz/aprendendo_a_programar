

from argparse import BooleanOptionalAction


great = 'Hello bob'
zap = great.lower()
print(zap)
print(great)

# lower() transforma os caracteres maiusculos de uma string em minusculos.
print('Hi There' .lower())

# capitaliza() transforma a primeira letra da string em maiuscula.
print('hello world'.capitalize())

# find() busca um conjunto de caracteres dentro da string e retorna a posição desse valor, se não encontrar o valor ele retorna -1
fruit = 'banana'
pos = fruit.find('ba')
print(pos)

# upper() transforma a string em letras garrafais
print(fruit.upper())
