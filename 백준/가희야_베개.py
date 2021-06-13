R, C = map(int, input().split())
Rg, Cg, Rp, Cp = map(int, input().split())
arr = [list(input()) for _ in range(R)]
pillow = Rp * Cp
p_count = 0

for item in arr:
    p_count += item.count('P')

print(1) if p_count < pillow else print(0)
