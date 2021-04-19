password = input()
result = ''

for i in password:
    asc = ord(i) + 2
    result += chr(asc)

print(result)
result = ''

for i in password:
    asc = ord(i) * 7 % 80 + 48
    result += chr(asc)

print(result)
