# 순차 탐색(Sequential Search)
# 리스트 중에서 원하는 데이터가 나올 때까지 데이터를 하나씩 비교해 탐색하는 방법

def sequential_search(data, search):
    for idx, item in enumerate(data):
        if item == search:
            return idx
    return -1

data_list = [1, 2, 5, 6, 10, 12, 25, 63]
print(sequential_search(data_list, 3))
