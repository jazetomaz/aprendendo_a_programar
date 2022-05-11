# 8.4 Abra o arquivo romeo.txt e leia linha por linha. Para cada linha, divida a linha em uma lista de palavras usando o método split(). O programa deve construir uma lista de palavras. Para cada palavra em cada linha, verifique se a palavra já está na lista e, se não, acrescente-a à lista. Quando o programa for concluído, classifique e imprima as palavras resultantes em ordem alfabética.

open(romeo.txt)

lst = list()
for line in fh:
    line.split()
    print(line.rstrip())
