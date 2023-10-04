string = input()
new_word = ""

word = ""
for char in string:
    if char == " ":
        if word:  
            new_word += word[-1]  
            word = ""  
    else:
        word += char 

if word:
    new_word += word[-1]

print(new_word)
