# 퀵 정렬(Quick sort)
# 기준점을 정해서 기준점보다 작은 건 왼쪽, 큰 건 오른쪽에 위치한다.

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right = list(), list()

    for i in range(1, len(data)):
        if data[i] < pivot:
            left.append(data[i])
            continue
        right.append(data[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([1, 1, 5, 3, 2, 9, 6, 5, 4, 12]))

# 코드 간결하게 쓰기
def q_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]

    return q_sort(left) + [pivot] + q_sort(right)

print(q_sort([1, 1, 5, 3, 2, 9, 6, 5, 4, 12]))
