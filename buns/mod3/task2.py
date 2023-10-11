a = int(input())
answer = bin(a)[2:] + ", " + oct(a)[2:] + ", " + hex(a)[2:]
print(answer)