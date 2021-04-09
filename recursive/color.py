r, g, b = map(int, input().split())
number_of_cases = r * g * b
arr = [0, 0, 0]
gb = g * b

for i in range(number_of_cases):
    arr[2] = i % b
    arr[1] = (i // b) % g
    arr[0] = i // gb
    print(arr[0], arr[1], arr[2])

print(number_of_cases)
