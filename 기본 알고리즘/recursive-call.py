# 재귀용법(Recursive call)
# 함수 내부에서 자기 함수를 호출하는 형태

# 재귀용법으로 팩토리얼 구현하기
def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num - 1)

print(factorial(3))

# 재귀용법으로 리스트 내부의 합 구하기
def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[-1] + sum_list(data[:-1])

print(sum_list([1, 2, 3, 4, 5]))

# 재귀용법으로 회문 판별하기
def palin(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palin(string[1:-1])

print(palin('tenet'))

# 숫자 1로 만들기
def make_it_the_number_1(num):
    print(num)
    if num <= 1:
        return num
    if num % 2 == 1:
        return make_it_the_number_1(3 * num + 1)
    return make_it_the_number_1(num // 2)

print(make_it_the_number_1(13))

# 정수를 1과 2와 3의 합으로 나타내기
def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    return func(data - 1) + func(data - 2) + func(data - 3)

print(func(5))
