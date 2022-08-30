# 삽입 정렬(Insertion sort)
# 두 번째 인덱스부터 키 값으로 지정, 앞의 인덱스에 위치한 데이터와 크기를 비교해서 더 작은 데이터가 나올 때까지 자리를 변경해가며 정렬

def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j - 1] <= data[j]:
                break
            data[j - 1], data[j] = data[j], data[j - 1]
    
    return data

print(insertion_sort([1, 1, 5, 3, 2, 9, 6, 5, 4, 12]))
