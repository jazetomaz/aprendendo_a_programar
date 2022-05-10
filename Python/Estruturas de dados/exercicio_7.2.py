fname = input("Enter file name: ")

fh = open(fname, 'r')
cont = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    cont = cont + 1
    print(line)

print(cont)

print("Done")
