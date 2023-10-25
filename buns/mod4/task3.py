def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

num1 = int(input('Введите первое число '))
num2 = int(input('Введите второе число '))
nod = euclid(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {nod}")