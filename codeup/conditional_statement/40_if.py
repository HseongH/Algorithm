h, w = map(float, input().split())
weight = 0

if h < 150:
    weight = h - 100
elif h < 160:
    weight = (h - 150) / 2 + 50
else:
    weight = (h - 100) * 0.9

percent = (w - weight) * 100 / weight

if percent <= 10:
    print('정상')
elif percent <= 20:
    print('과체중')
else:
    print('비만')
