def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = fast_power(a, n // 2)
        return half_power * half_power
    else:
        return a * fast_power(a, n - 1)

a = int(input('Введите число '))
n = int(input('Введите в степень '))
result = fast_power(a, n)
print(f"{a}^{n} = {result}")