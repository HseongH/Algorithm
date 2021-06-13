test_case = int(input())

for _ in range(test_case):
    n = int(input())
    init = input()
    target = input()

    rev = abs(init.count('W') - target.count('W'))  # 뒤집어야 하는 돌의 개수
    swap = 0

    for i in range(n):
        if init[i] != target[i]:
            swap += 1   # 서로 다른 부분
                        # 서로 다른 부분 - 뒤집어야 하는 돌의 개수 = 서로 바꿀 수 있는 돌의 개수
                        # (서로 다른 부분 - 뒤집어야 하는 돌의 개수) // 2 = 돌을 변경하는 횟수

    print((swap - rev) // 2 + rev)
