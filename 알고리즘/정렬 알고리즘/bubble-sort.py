# 버블 정렬 (Bubble sort)
# 리스트 안의 요소들을 두개씩 차례로 비교해서 앞의 요소가 뒤의 요소보다 크다면 자리를 바꾼다.
# 특이점
# 1. 반복이 한 번 완료될 때마다 맨 뒤의 요소가 결정된다.
# 2. 입력이 n이라면 n - 1번 반복 시 정렬이 완료된다.
# 3. 자리 변경이 한 번도 일어나지 않으면 정렬이 완료된 것으로 간주된다.

def bubble_sort(data):
    for i in range(len(data) - 1):
        swap = False
        
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True
        
        if not swap:
            break
    
    return data

print(bubble_sort([1, 1, 5, 3, 2, 9, 6, 5, 4, 12]))
