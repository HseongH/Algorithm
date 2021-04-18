import re

p1 = re.compile('\(')
p2 = re.compile('\)')

inp = input()

m = p1.findall(inp)
n = p2.findall(inp)

print(len(m), len(n))
