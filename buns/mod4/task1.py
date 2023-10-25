numbers = input("Введите числа через пробел: ").split()

numbers = [int(num) for num in numbers]

if len(numbers) == 0:
    print("Список пуст")
elif len(set(numbers)) == 1:
    print("Все числа равны")
elif len(set(numbers)) == len(numbers):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")