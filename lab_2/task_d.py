def f(a,b,c,d,x):
    return a*x**3 + b*x**2 + c*x + d



a,b,c,d = map(int, input().split())
eps = 1e-10
left = -10**6
right = 10**6

while (right - left) > eps:
    middle = (left + right) / 2
    if a > 0:
        if f(a,b,c,d,middle) <= 0:
            left = middle
        else:
            right = middle
    else:
        if f(a,b,c,d,middle) <= 0:
            right = middle
        else:
            left = middle

print(middle)