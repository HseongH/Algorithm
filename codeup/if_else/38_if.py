num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
c = 0
arr = [0, 5, 4, 3, 2, 1]

for i in range(6):
    for j in num2:
        if num1[i] == j:
            c += 1

if c == 6:
    print(1)
elif c == 5:
    for i in num2:
        if num1[len(num1) - 1] == i:
            c += 1

    if c == 6:
        print(2)
    else:
        print(3)
elif c == 4:
    print(4)
elif c == 3:
    print(5)
else:
    print(0)
