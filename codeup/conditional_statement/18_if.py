i_age = int(input())
year = 2013 - i_age
p_age = year % 100

s = 1 if year // 100 == 19 else 3

print(p_age, s)
