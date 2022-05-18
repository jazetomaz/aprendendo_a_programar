from itertools import count


counts = dict()
names = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
names = names.split()

for name in names:
    counts[name] = counts.get(name, 0) + 1


print(counts)
