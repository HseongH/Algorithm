import re

string = input()

p = re.compile('love')
result = p.findall(string)

print(len(result))
