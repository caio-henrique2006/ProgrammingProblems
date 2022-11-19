m, n, a = map(int, input().split())
soma = 0
if a >= m and a >= n:
    soma = 1
else:
    if m % a != 0:
        soma += m//a + 1
    else:
        soma += m//a

    if n % a != 0:
        soma += n//a + 1
    else:
        soma += n//a

print(soma)