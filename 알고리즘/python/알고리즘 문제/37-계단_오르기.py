from sys import stdin

input = stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]
score = list()

score.append(stairs[0])
if n >= 2: score.append(stairs[0] + stairs[1])
if n >= 3: score.append(max(stairs[2] + stairs[0], stairs[2] + stairs[1]))

for i in range(3, n):
    score.append(max(stairs[i] + score[i - 2], stairs[i] + stairs[i - 1] + score[i - 3]))

print(score[n - 1])
