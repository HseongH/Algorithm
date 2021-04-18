n = int(input())
arr = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    
    arr.append((name, score))

arr.sort(key=lambda x: (x[1]), reverse=True)

print(arr[2][0])
