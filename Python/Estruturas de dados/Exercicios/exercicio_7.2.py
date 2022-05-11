fname = input("Enter file name: ")
fh = open(fname)
cont = 0


for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    zpos = line.find(':')
    line = line[zpos + 1:]
    num = float(line)
    soma = soma + num
    cont = cont + 1

print('Average spam confidence: ', soma / cont)
