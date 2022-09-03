import re

n = int(input())
count = 0

for _ in range(n):
    string = input()

    for char in string:
        group = re.findall(f'{char}+', string)
        
        if len(group) > 1:
            break
    else:
        count += 1

print(count)
