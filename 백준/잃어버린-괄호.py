calculation = [[int(n) for n in i.split('+')] for i in input().split('-')]
result = sum(calculation[0])

for i in range(1, len(calculation)):
    result -= sum(calculation[i])

print(result)
