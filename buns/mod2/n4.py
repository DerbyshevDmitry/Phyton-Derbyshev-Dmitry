n = int(input('Введите число '))
fn = n
bin_n = ''
oct_n = ''
hex_n = ''
hex_characters = "0123456789ABCDEF"
assert n > 0, 'Неверный ввод'
while n > 0:
    bin_n = str(n % 2) + bin_n
    n //= 2
print('n в двоичной системе счисления', bin_n)
n = fn
while n > 0:
    oct_n = str(n % 8) + oct_n
    n //= 8
print('n в восьмиричной системе счисления', oct_n)
n = fn   
while n > 0:
    remainder = n % 16
    hex_n =  hex_characters[remainder] + hex_n
    n //= 16
print('n в шестнадцатиричной системе счисления', hex_n)

