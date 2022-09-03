T = int(input())

for _ in range(T):
    students = list(map(int, input().split()))
    aver = sum(students[1:]) / students[0]

    print('%.3f%%' % (len(list(filter(lambda x: x > aver, students[1:]))) / students[0] * 100))
