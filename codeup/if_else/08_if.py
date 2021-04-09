distance = int(input())
conditions = [
    50 <= distance and distance <= 70,
    distance % 6 == 0
]

print('win') if True in conditions else print('lose')
