string = input().upper()
alpha_list = [0] * 26

for char in string:
    index = ord(char) - ord('A')
    alpha_list[index] += 1

mode = max(alpha_list)
mode_count = alpha_list.count(mode)

print(chr(alpha_list.index(mode) + ord('A'))) if mode_count == 1 else print('?')
