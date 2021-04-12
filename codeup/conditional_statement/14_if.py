time, c_score = map(int, input().split())
r_time = 90 - time
p_score = r_time // 5
p_score = p_score + 1 if r_time % 5 != 0 else p_score + 0

print(c_score + p_score)
