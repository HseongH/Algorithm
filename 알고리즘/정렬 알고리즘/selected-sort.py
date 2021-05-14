# 선택 정렬(Selected sort)
# 반복 문을 반복할 때마다 리스트 내의 최소값을 찾아 그 값을 제일 앞의 인덱스 요소와 서로 교체한다.

def selected_sort(data):
    for i in range(len(data) - 1):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        if min != i:
            data[min], data[i] = data[i], data[min]

    return data

print(selected_sort([1, 1, 5, 3, 2, 9, 6, 5, 4, 12]))
