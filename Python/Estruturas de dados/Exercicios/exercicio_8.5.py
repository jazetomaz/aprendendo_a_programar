from fnmatch import fnmatchcase
from subprocess import STARTF_USESHOWWINDOW


fname = input('Insira o nome do arquivo:  ')
if len(fname) < 1:
    fname('mbox-short.txt', 'r')
cont = 0
fh = open(fname)
cont = 0

for line in fh:
    if not line.startswith('From '):
        continue
    cont = cont + 1
    line = line.split()
    print(line[1])

print('There were ', cont, 'lines in the file with From as the first word')
