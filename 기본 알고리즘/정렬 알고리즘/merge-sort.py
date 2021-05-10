# 병합 정렬(Merge sort)
# 리스트를 비슷한 크기의 두 부분으로 나눈다.
# 더 이상 나눌 수 없을 때까지 리스트를 나눈 후 정렬하여 다시 합친다.

def splitmerge(data):
    if len(data) <= 1:
        return data
    center = len(data) // 2
    left = splitmerge(data[:center])
    right = splitmerge(data[center:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    left_p = 0
    right_p = 0

    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            sorted_list.append(left[left_p])
            left_p += 1
        else:
            sorted_list.append(right[right_p])
            right_p += 1

    while left_p < len(left):
        sorted_list.append(left[left_p])
        left_p += 1

    while right_p < len(right):
        sorted_list.append(right[right_p])
        right_p += 1

    return sorted_list

print(splitmerge([1, 1, 5, 3, 2, 9, 6, 5, 4, 12]))
