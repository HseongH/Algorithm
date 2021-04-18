n1 = input()

f = open('text1.txt', 'w')
f.write(input())
f.close()

n2 = input()

f = open('text2.txt', 'w')
f.write(input())
f.close()

f = open('text1.txt', 'r')
arr1 = list(map(int, f.readline().split()))
f.close()

f = open('text2.txt', 'r')
arr2 = list(map(int, f.readline().split()))
f.close()

ans = list(map(lambda x: x in arr1, arr2))

for i in ans:
    print('%d' % i, end=' ')
