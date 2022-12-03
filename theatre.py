n, m, a = map(int, input().split())

if n%a != 0:
    v1 = n//a + 1
else:
    v1 = n//a

if m%a != 0:
    v2 = m//a + 1
else:
    v2 = m//a

print(v1*v2)