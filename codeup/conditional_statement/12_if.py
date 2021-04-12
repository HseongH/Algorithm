y, m, d = map(int, input().split())
birth = (y + m + d) // 100

print('대박') if birth % 2 == 0 else print('그럭저럭')

