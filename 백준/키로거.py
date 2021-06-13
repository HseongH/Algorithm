test_case = int(input())

for _ in range(test_case):
    L = input()
    left, right = list(), list()

    for s in L:
        if s == '-':
            if left:
                left.pop()
        elif s == '<':
            if left:
                right.append(left.pop())
        elif s == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(s)
    
    left.extend(reversed(right))
    print(''.join(left))
