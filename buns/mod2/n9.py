string = input()
vowels = 'уеыаоэяиюЁУЕЫАОЭЯИЮ'
consonants = 'йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ'
vowel_count = 0
consonants_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonants_count += 1
print(vowel_count)
print(consonants_count)
