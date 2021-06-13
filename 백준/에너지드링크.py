n = int(input())
energy = list(map(int, input().split()))
energy.sort(reverse=True)

amount = energy[0]

for i in range(1, n):
    amount += energy[i] / 2

print('%g' % amount)
