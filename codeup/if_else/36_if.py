from math import ceil

time, score1, score2 = map(int, input().split())
score1 = ceil((90 - time) / 5) + score1

if score1 > score2:
    print('win')
elif score1 < score2:
    print('lose')
else:
    print('same')
