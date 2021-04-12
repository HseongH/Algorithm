state = input().split()
score = ['모', '도', '개', '걸', '윷']
c = 0

for i in state:
    if i == '0':
        continue
    c += 1

print(score[c])
