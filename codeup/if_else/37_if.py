a, b, c, d = map(int, input().split())
div1, div2 = a / b, c / d
out = ['>', '=', '<']
condition = [
    div1 > div2,
    div1 == div2,
    div1 < div2
]

print(out[condition.index(True)])
