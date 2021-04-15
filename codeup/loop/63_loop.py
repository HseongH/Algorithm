k = int(input())

for i in range(1, k):
    if i <= 6 and (k - i) <= 6:
        print(i, k - i)
