domain = input("Введите доменное имя сайта: ")
current_domain = ""

for char in domain:
    if char == ".":
        if current_domain:
            print(current_domain)
            current_domain = ""
    else:
        current_domain += char

if current_domain:
    print(current_domain)
    
