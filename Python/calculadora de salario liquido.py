from math import trunc


sbruto = int(input('Informe o salario bruto:    '))
inss = round(sbruto * 8.24/100, 2)
irrf = sbruto * 1/100
vr = 105
vt = sbruto * 8/100

sliq = trunc(sbruto - inss - irrf - vr - vt, 2)

print('Seu salario liquido é:', sliq)

print(sliq + 700)
