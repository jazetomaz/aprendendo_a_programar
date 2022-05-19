# 9.4 Escreva um programa para ler o mbox-short.txt e descobrir quem enviou o maior número de mensagens de correio. O programa procura por linhas 'De ' e toma a segunda palavra dessas linhas como a pessoa que enviou o e-mail. O programa cria um dicionário Python que mapeia o endereço de e-mail do remetente para uma contagem do número de vezes que aparecem no arquivo. Depois que o dicionário é produzido, o programa lê o dicionário usando um loop máximo para encontrar o committer mais prolífico.

name = input('Enter file:')
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('From:'):
        continue
    line = line.split()
    line = line[1]
    counts[line] = counts.get(line, 0) + 1

bigvalor = None
bigmail = None

for mail, valor in counts.items():
    print(max(valor))
    if bigvalor is None or valor > bigvalor:
        bigvalor = valor
        bigmail = mail


#print(bigmail, bigvalor)
