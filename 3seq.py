stsps1 = input("Введите элементы 1-го списка через запятую : ")
stsps2 = input("Введите элементы 2-го списка через запятую : ")
spis1 = stsps1.split(',')
spis2 = stsps2.split(',')

#print(spis1)
#print(spis2)

for it2 in spis2:
    if it2 in spis1:
        spis1.remove(it2)

print(spis1)
