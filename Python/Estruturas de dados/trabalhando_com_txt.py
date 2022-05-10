fname = input('Enter the file name:     ')
count = 0
try:
    fhand = open(fname, 'r')
except:
    print('Arquivo não encontrado, tente novamente  ')
    quit()


#inp = fhand.read()
# print(len(inp))
# print(inp[0:999])

for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'Subject lines in', fname)


# for line in fhand:
#   line = line.rstrip()
#   if not '@uct.ac.za' in line:
#      continue
#  print(line)
