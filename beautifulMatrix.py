matriz = []
somaFinal = 0
for x in range(5):
    entrada = list(input().split())
    matriz.append(entrada)

# Localizar:
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        if matriz[x][y] == '1':
            coordenada = [x, y]

# Calcular:
if coordenada[0] > 2:
    somaFinal += coordenada[0] - 2 
else:
    somaFinal += 2 - coordenada[0]
    
if coordenada[1] > 2:
    somaFinal += coordenada[1] - 2
else:
    somaFinal += 2 - coordenada[1]
print(somaFinal)