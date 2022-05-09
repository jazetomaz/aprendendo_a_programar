# replace() serve para buscar um conjunto de caracteres na string e substituilo.
great = 'Hello Bob'
nstr = great.replace('Bob', 'Jane')
print(great)
print(nstr)

nstr = great.replace('o', 'X')
print(nstr)

# lstrip() remove os espaços a esquerda, rstrip() remove os espaços a direita, strip() remove os espaços das extremidades.

great1 = '      hello bob       '
great2 = great1.lstrip()
great3 = great1.rstrip()
great4 = great1.strip()

print(great1)
print(great2)
print(great3)
print(great4)
