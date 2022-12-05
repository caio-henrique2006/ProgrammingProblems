n = int(input())
matriz = []
somaTotal = 0
for x in range(n):
    entrada = list(input().split())
    matriz.append(entrada)
print(matriz)
if n >= 3:
    for x in range(len(matriz[0])):
        for y in range(len(matriz[0])):
            somaTotal += int(matriz[x][y])
    print(somaTotal)
else:
    soma1 = int(matriz[0][0]) + int(matriz[1][1]) + int(matriz[1][0])
    soma2 = int(matriz[0][0]) + int(matriz[1][1]) + int(matriz[0][1])
    if soma1 > soma2:
        print(soma1)
    else:
        print(soma2)
