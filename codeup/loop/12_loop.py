integer = int(input())

for i in range(2, integer):
    if integer % i == 0:
        print('not prime')
        break
else:
    print('prime')
