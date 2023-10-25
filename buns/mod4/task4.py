def create_palindrome(word):
    # Создаем словарь для подсчета количества каждой буквы в слове
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    # Определяем количество букв которые появляются нечетное количество раз
    odd_count = 0
    odd_letter = ""
    for letter, count in letter_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_letter = letter
    # Если более одной буквы появляются нечетное количеством раз, палиндром невозможен
    if odd_count > 1:
        return None
    # Составляем палиндром
    palindrome = ""
    for letter, count in letter_count.items():
        if count % 2 == 0:
            palindrome += letter * (count // 2)
    palindrome = palindrome + odd_letter * (odd_count) + palindrome[::-1]

    return palindrome

word = input('Введите слово: ')
result = create_palindrome(word)
if result:
    print(f"Можно составить палиндром: {result}")

else:
   print("Из данного слова невозможно составить палиндром.")