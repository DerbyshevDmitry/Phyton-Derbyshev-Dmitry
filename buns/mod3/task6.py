str = input()
answer = ''.join(i[-1] for i in str.split())
print(answer)