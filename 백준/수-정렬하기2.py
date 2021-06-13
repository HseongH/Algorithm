from sys import stdin

def splitmerge(data):
    if len(data) <= 1:
        return data

    center = len(data) // 2
    left = splitmerge(data[:center])
    right = splitmerge(data[center:])

    return merge(left, right)

def merge(left, right):
    sorted_list = list()
    left_p, right_p = 0, 0

    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            sorted_list.append(left[left_p])
            left_p += 1
            continue
        sorted_list.append(right[right_p])
        right_p += 1

    while left_p < len(left):
        sorted_list.append(left[left_p])
        left_p += 1

    while right_p < len(right):
        sorted_list.append(right[right_p])
        right_p += 1

    return sorted_list

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
arr = splitmerge(arr)

print('\n'.join(map(str, arr)))
