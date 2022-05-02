from operator import truediv

# Variavel boleana ou lógica é um tipo de variavel que só pode ter dois valores, sendo eles 'True' ou 'False'. Verdadairo ou falso

found = False
print('Antes', found)
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i == 5:
        found = True
    print(i, found)


print('Depois', found)
