size = int(input())
print('Исходная матрица')
for i in range(1, size+1):
    for j in range(1, size+1):
        if j != size:
            print(j, end=', ')
        else:
            print(j)
print('Транспонированная матрица')
for i in range(1, size+1):
    for j in range(1, size+1):
        if j != size:
            print(i, end=', ')
        else:
            print(i)
