a, b = map(int, input().split())

def size(a, b):
    if a > b:
        print('>')
        return
    if a < b:
        print('<')
        return
    print('=')

size(a, b)
