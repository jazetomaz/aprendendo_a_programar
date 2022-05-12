# 8.4 Abra o arquivo romeo.txt e leia linha por linha. Para cada linha, divida a linha em uma lista de palavras usando o método split(). O programa deve construir uma lista de palavras. Para cada palavra em cada linha, verifique se a palavra já está na lista e, se não, acrescente-a à lista. Quando o programa for concluído, classifique e imprima as palavras resultantes em ordem alfabética.


from os import fsdecode
from tkinter import N


fname = input("Enter file name: ")
fh = open(fname)
fh = fh.read()
fh = fh.split()

lst = list()

for i in fh:
    if not i in lst:
        lst.append(i)

lst.sort()
print(lst)
