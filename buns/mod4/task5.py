def statistics(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    letter_counts = {}
    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1])

    with open(output_file, 'w') as output:
        for letter, count in sorted_letter_counts:
            output.write(f"{letter}: {count}\n")

    print(f"Статистика успешно записана в файл '{output_file}'.")


input_filename = input('Укажите имя входного файла: ')
output_filename = input('Укажите имя файла для записи результатов: ')
statistics(input_filename, output_filename)