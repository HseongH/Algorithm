# 동적 계획법(Dynamic Programming)
# 어떤 문제를 해결할 때 작은 부분부터 해결한 후 그 결과 값을 이용해 큰 문제를 해결해가는 기법
# Memoization: 프로그램 실행 시 이전의 결과 값을 저장하여 중복된 연산을 실행하지 않도록 하여 프로그램 수행 속도를 빠르게 하는 기법

# 동적 계획법으로 피보나치 수열 계산 함수 구하기
# 재귀용법으로 구현하기
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

# 동적 계획법으로 구현하기
def fibo(num):
    if num <= 1:
        return num
    
    arr = [0 for _ in range(num + 1)]
    arr[1] = 1

    for i  in range(2, num + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[num]

for i in range(1, 11):
    print(fibonacci(i))
    print(fibo(i))
