i = input('Введите i ')
n = int(input('Введите n '))
def shift_character(i, n):
    alphabet_size = 26
    i_value = ord(i) - ord('a')  
    shifted_value = (i_value + n) % alphabet_size  
    k = chr(shifted_value + ord('a'))  
    return k
print('k =',shift_character(i, n))
