string = input()
match = ['c', 'C']

c_count = 0
cc_count = 0

for i in range(len(string)):
    if string[i] in match:
        c_count += 1
        if i < len(string) - 1 and string[i + 1] in match:
            cc_count += 1

print(c_count)
print(cc_count)
