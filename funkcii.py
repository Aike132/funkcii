def minim(a, b, c):
    if a < b:
        min = a
    else:
        min = b
    if min > c:
        min = c
    return min

a = input()
b = input()
c = input()
print(minim(a,b,c))


def kolvo(g):
    k = 0
    while g > 0:
        k = k+1
        g = g//10
    return k

f = int(input())
print(kolvo(f))


def summa(n):
    i=0
    s=0
    while i <= n:
        s = s+i
        i = i+1
    return s

n = int(input())
print(summa(n))


def faсt(t):
    i = 1
    f = 1
    while i <= t:
        f = f * i
        i = i + 1
    return f


t = int(input())
print(faсt(t))