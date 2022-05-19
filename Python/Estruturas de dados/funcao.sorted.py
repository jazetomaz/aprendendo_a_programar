# a função sorted() classifica os itens do menor para o maior, considerando o primeiro caractere da variavel, caso seja equivale ela considera o primeiro e segundo e assim sucessivamente até encontrar a diferença.


d = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
dict_items = ([('a', 10), ('c', 22), ('b', 1)])
# print(sorted(dict_items))

# classificando por itens
# for k, v in sorted(d.items()):
#    print(k, v)

# classificando por valor dos items
for k, v in sorted(d.items()):
    tmp.append((v, k))

tmp = sorted(tmp, reverse=True)
print(tmp)
