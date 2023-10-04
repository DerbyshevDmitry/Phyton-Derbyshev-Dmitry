string = input()
sum_1 = 0
sum_0 = 0
for i in string:
    if int(i) == 0:
        sum_0 += 1
    if int(i) == 1:
        sum_1 += 1
if sum_0 == sum_1:
    print('yes')
else:
    print('no')
