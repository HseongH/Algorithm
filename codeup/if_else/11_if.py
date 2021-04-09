y, m, d = map(int, input().split())
birth = y - m + d

print('대박') if birth % 10 == 0 else print('그럭저럭')
