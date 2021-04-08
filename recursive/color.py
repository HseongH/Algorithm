r, g, b = map(int, input().split())
arr = [0] * 3

def color():
    while arr[0] < r:
        arr[2] = 0

        for i in range(b):
            arr[2] = i
            print(arr[0], arr[1], arr[2])

        arr[1] += 1
        
        if arr[1] > g - 1:
            arr[1] = 0
            arr[0] += 1

        color()

color()
print(r * g * b)
