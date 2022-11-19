def progressaoAritmetica(a, b, n):
    value = (n*(a+b))/2
    return value
def progressaoGeometrica(a, b, k):
    value = (b*k-a)/(k-1)
    return value

n = int(input())
if n == 1:
    a, b, n = map(int, input().split())
    resultado = progressaoAritmetica(a, b, n)
    print(resultado)
else:
    a, b, n = map(int, input().split())
    resultado = progressaoGeometrica(a, b, n)
    print(resultado)