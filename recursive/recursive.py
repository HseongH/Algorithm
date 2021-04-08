# # 재귀 알고리즘
# # 어떠한 이벤트에서 자기 자신을 포함하고 다시 자기 자신을 사용하여 정의되는 경우를 말한다.

# # factorial

# def factorial(n: int) -> int:
#     if n > 0:
#         return n * factorial(n - 1)
#     return 1

# """입력하는 수가 0과 같거나 작아 1이 리턴될 때 까지 factorial 함수를 호출한다.
#    1이 리턴되면 그 때 부터 n이 처음 입력된 수와 같아질 때까지  n * n - 1을 수행해 그때까지의 연산 결과를 최종 반환한다."""

# # 유클리드 호제법

# def gcd(x: int, y: int) -> int:
#     if y == 0:
#         return x
#     return gcd(y, x % y)

# """최대 공약수를 구할 때 사용하는 알고리즘으로 두 수를 각 변으로 가지는 가상의 직사각형을 만들고, 더 이상 직사각형이 나오지 않을 때(입력되는 x % y == 0)까지 함수를 수행한다."""

# # 하노이의 탑

# def move(no: int, x: int, y: int) -> None:
#     if no > 1:
#         move(no - 1, x, 6 - x - y)

#     print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

#     if no > 1:
#         move(no - 1, 6 - x - y, y)

# """원반이 있고, 기둥이 3개 존재할 때 한 번에 한 원반씩 옮겨 초기 기둥에서 이동할 기둥으로 이동한다. 단, 크기가 작은 원반 위로 크기가 큰 원반이 올라올 수는 없다."""

# # 8퀸 문제

# pos = [0] * 8

# def put() -> None:
#     for i in range(8):
#         print(f'{pos[i]:2}', end='')
#     print()

# def set(i: int) -> None:
#     for j in range(8):
#         pos[i] = j
#         if i == 7:
#             put()
#         else:
#             set(i + 1)

# set(0)

# pos = [0] * 8
# flag = [False] * 8

# def put() -> None:
#     for i in range(8):
#         print(f'{pos[i]:2}', end='')
#     print()

# def set(i: int) -> None:
#     for j in range(8):
#         if not flag[i]:
#             pos[i] = j
#             if i == 7:
#                 put()
#             else:
#                 flag[j] = True
#                 set(i + 1)
#                 flag[j] = False

# set(0)

pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put() -> None:
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()

def set(i: int) -> None:
    for j in range(8):
        if(     not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)

"""8개의 퀸이 존재하고 8 * 8의 체스판에 퀸끼리 서로 공격할 수 없도록 배치한다."""
