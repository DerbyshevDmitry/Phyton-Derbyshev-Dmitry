input_phone = input()

cleaned_phone = ""

for char in input_phone:
    if char.isdigit() or char == "+":
        cleaned_phone += char

print(cleaned_phone)
