# 이진 탐색(Binary Search)
# 정렬이 완료된 리스트에서 원하는 데이터를 찾는 방법
# 리스트를 두 부분으로 나누어 데이터가 있을 만한 곳을 탐색한다.

# index 번호 탐색
def bin_search(data, search):
    pl = 0
    pr = len(data) - 1

    while True:
        pc = (pl + pr) // 2
        if data[pc] == search:
            return pc
        elif data[pc] < search:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break

    return -1

# contains 여부 탐색
def binary_search(data, search):
    while len(data) > 0:
        pc = len(data) // 2
        if data[pc] == search:
            return True
        elif data[pc] < search:
            data = data[pc + 1:]
        else:
            data = data[:pc]
    return False

# 재귀용법으로 구현
def recur_bin_search(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    elif len(data) == 1 and data[0] != search:
        return False
    elif len(data) <= 0:
        return False
    
    pc = len(data) // 2
    if data[pc] == search:
        return True
    elif data[pc] < search:
        return recur_bin_search(data[pc + 1:], search)
    else:
        return recur_bin_search(data[:pc], search)

data_list = [1, 2, 5, 6, 10, 12, 25, 63]
print(recur_bin_search(data_list, 3))
