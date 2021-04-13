string = input()
result = ''

for i in string:
    if i == i.upper():
        result += i.lower()
        continue
    if i == i.lower():
        result += i.upper()
        continue
    result += i

print(result)
