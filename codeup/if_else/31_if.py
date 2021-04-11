s1, s2 = map(int, input().split())
menu = [400, 340, 170, 100, 70]
cal = menu[s1 - 1] + menu[s2 - 1]

print('angry') if cal > 500 else print('no angry')
