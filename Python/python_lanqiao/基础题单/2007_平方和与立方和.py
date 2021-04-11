# 2007平方和与立方和

a, b = map(int, input().split())
x, y = 0, 0
if a > b:
    a, b = b, a
for i in range(a, b+1):
    if i % 2 == 0:
        x += i**2
    else:
        y += i**3
print(x, y)
