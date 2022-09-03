import re

string = input()
string = re.sub('c=|c-|dz=|d-|lj|nj|s=|z=', ' ', string)

print(len(string))
