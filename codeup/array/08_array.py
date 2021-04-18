string = input()
alphabet = [0] * 26

for i in string:
    n = ord(i)

    if n < 97 or n > 122:
        continue

    alphabet[n - 97] += 1

for i, value in enumerate(alphabet):
    print('%s:%d' % (chr(i + 97), value))
