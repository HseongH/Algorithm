string = input()
zero_split = len([s for s in string.split('0') if s])
one_split = len([s for s in string.split('1') if s])

print(zero_split) if zero_split < one_split else print(one_split)
