string = input()

if string:
    first_char = string[0]
    sum1 = 1
    for char in string[1:]:
        if char == first_char:
            sum1 += 1
        else:
            break
    print(sum1)
else:
    print('')
