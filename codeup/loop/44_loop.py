string = input()
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(string)):
    if string[i] != ' ':
        idx = (alpabet.index(string[i]) - 3) % len(alpabet)
        print(alpabet[idx], end='')
        continue
    print(string[i], end='')
    
