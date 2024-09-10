kolsp = int(input('Введите количество элементов списка : '))
sp = []

for teksp in range(1, kolsp+1):
    tekel = int(input(f'Введите {teksp} элемент : '))
    sp.append(tekel)

print(sp)