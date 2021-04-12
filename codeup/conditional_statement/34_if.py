a, b, c = map(int, input().split())
b = b - c

if a > b:
    print('do not advertise')
elif a < b:
    print('advertise')
else:
    print('does not matter')
