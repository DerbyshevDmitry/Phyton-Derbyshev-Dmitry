string = input()
def duplicate(strg):
    for i in range(len(string)):
        for k in range(i + 1, len(string)):
            if string[i] == string[k]:
                return True
            
    return False

print(duplicate(string))
