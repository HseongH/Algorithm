from hashlib import sha256

string = input()
print(sha256(string.encode()).hexdigest())
