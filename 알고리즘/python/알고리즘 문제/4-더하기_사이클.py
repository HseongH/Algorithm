n = int(input())
num = n
count = 0

while True:
    temp = (num // 10 + num % 10) % 10
    num = num % 10 * 10 + temp
    count += 1

    if num == n:
        print(count)
        break
