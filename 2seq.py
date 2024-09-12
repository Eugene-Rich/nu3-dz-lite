stsps = input("Введите элементы списка через запятую : ")
stsps = stsps.replace(';', ',')
stsps = stsps.replace('/', ',')
stsps = stsps.replace(' ', '')

spis = stsps.split(',')

spis_uniq = []
for iss1 in range(len(spis)):
    fl = True
    for iss2 in range(len(spis)):
        if iss1 != iss2 and spis[iss1] == spis[iss2]:
            fl = False
            break
    if fl:
        spis_uniq.append(spis[iss1])

print(spis_uniq)

