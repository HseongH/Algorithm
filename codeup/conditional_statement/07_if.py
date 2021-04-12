distance = int(input())
conditions = [
    30 <= distance and distance <= 40,
    60 <= distance and distance <= 70
]

print('win') if True in conditions else print('lose')
