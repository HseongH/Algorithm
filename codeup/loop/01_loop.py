str1, str2 = input().split()
string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s_idx = string.index(str1)
e_idx = string.index(str2)

for i in range(s_idx, e_idx + 1):
    print(string[i], end=' ')
