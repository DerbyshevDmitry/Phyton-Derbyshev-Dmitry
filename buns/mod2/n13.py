string = input()
sum1 = 0
sum2 = 0
for i in range(len(string)):
    k = int(string[i])
    if i % 2 == 0:
        sum1 += k
    else:
        sum2 += k
   
if (sum1 + sum2 * 3) % 10 == 0:
    print('yes')
else:
    print('no')
