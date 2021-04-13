formula = input()
sign = ['+', '-', '*', '/', '=']
result = 0
term = 0

for i, num in enumerate(formula):
    if num in sign:
        n = formula[term:i]

        if formula[term - 1] == '-':
            result -= int(n)
        elif formula[term - 1] == '*':
            result *= int(n)
        elif formula[term - 1] == '/':
            result //= int(n)
        else:
            result += int(n)

        term = i + 1

print(result)
