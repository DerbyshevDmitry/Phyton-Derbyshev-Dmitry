a_b_c = input()
ind1 = a_b_c.find(" ")
a = int(a_b_c[:ind1])
ind2 = a_b_c.find(" ", ind1+1)
b = int(a_b_c[ind1+1:ind2])
c = int(a_b_c[ind2+1:])
assert -1000 <= a <= 1000, "Неверное значение a"
assert -1000 <= b <= 1000, "Неверное значение b"
assert -1000 <= c <= 1000, "Неверное значение c"
if a > b:
    if c > a:
        print(a)
    elif c > b:
        print(c)
    else:
        print(b)
elif b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    print(b)
