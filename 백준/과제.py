# n = int(input())
# problems = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1], reverse=True)
# total_point = [0 for _ in range(max(problems)[0])]

# for problem in problems:
#     while total_point[problem[0] - 1] > 0 and problem[0] > 0:
#         problem[0] -= 1
#     if problem[0] > 0:
#         total_point[problem[0] - 1] = problem[1]

# print(sum(total_point))

# 정섭님 코드 참고해서 heapq로도 풀 수 있었습니다. 감사합니다.

import heapq

n = int(input())
problems = []

for _ in range(n):
    problem = list(map(int, input().split()))
    heapq.heappush(problems, [-problem[1], problem[0]])

complete = [0 for _ in range(max(problems, key=lambda x: x[1])[1])]

while problems:
    problem = heapq.heappop(problems)

    for i in range(problem[1], 0, -1):
        if complete[i - 1] == 0:
            complete[i - 1] = problem[0]
            break

print(abs(sum(complete)))
