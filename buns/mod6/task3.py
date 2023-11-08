def is_amstrong_number(a):
    prev_a = a
    numbers = []
    while a     != 0:
        numbers.append(a % 10)
        a //= 10
    length = len(numbers)
    ans = 0
    for number in numbers:
        ans += number**length
    return (ans == prev_a)

ind_armstrong = 10

def get_armstrong_numbers():
    global ind_armstrong
    while not is_amstrong_number(ind_armstrong):
        ind_armstrong += 1
    print(ind_armstrong, end=' ')
    ind_armstrong += 1

for i in range(8):
    get_armstrong_numbers()