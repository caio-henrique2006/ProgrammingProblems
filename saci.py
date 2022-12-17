'''
PosiçãoInicial, percorre os 1's que pode escolher, se mais de um, acrescenta na lista 
de caminhos possíveis, percorre o primeiro caminho, se levar até o final aceita, se n, retorna a
lista e olha para o próximo caminho.
'''
# Olhar envolta:
def lookAround(posicao, caminho_possivel, mapa):
    print(posicao)
    # Observando os 4 polos:
    if posicao[0]+1 <= N-1 and mapa[posicao[0]+1][posicao[1]] == "1":
        caminho_possivel.append([posicao[0]+1, posicao[1]])
    if posicao[0]-1 >= 0 and mapa[posicao[0]-1][posicao[1]] == "1":
        caminho_possivel.append([posicao[0]-1, posicao[1]])
    if posicao[1]+1 <= M-1 and mapa[posicao[0]][posicao[1]+1] == "1":
        caminho_possivel.append([posicao[0], posicao[1]+1])
    if posicao[1]-1 >= 0 and mapa[posicao[0]][posicao[1]-1] == "1":
        caminho_possivel.append([posicao[0], posicao[1]-1])
    return caminho_possivel

# Percorre os caminhos_possiveis:
def runner(caminho_possivel, contador_caminhos, posicao):
    c = True
    d = True
    P_inicial = posicao
    while c:
        caminho_passado = P_inicial
        contador_passos = 0
        caminho_escolhido = caminho_possivel[contador_caminhos]
        posicao = caminho_escolhido
        contador_caminhos += 1
        while d:
            temp = posicao
            if (posicao[0]+1 <= N-1 and (mapa[posicao[0]+1][posicao[1]] == "1" or mapa[posicao[0]+1][posicao[1]] == "3")
            and mapa[posicao[0]+1][posicao[1]] != mapa[caminho_passado[0]][caminho_passado[1]]):
                posicao = [posicao[0]+1, posicao[1]]
            elif (posicao[0]-1 >= 0 and (mapa[posicao[0]-1][posicao[1]] == "1" or mapa[posicao[0]-1][posicao[1]] == "3")
            and mapa[posicao[0]-1][posicao[1]] != mapa[caminho_passado[0]][caminho_passado[1]]):
                posicao = [posicao[0]-1, posicao[1]]
            elif (posicao[1]+1 <= M-1 and (mapa[posicao[0]][posicao[1]+1] == "1" or mapa[posicao[0]][posicao[1]+1] == "3")
            and mapa[posicao[0]][posicao[1]+1] != mapa[caminho_passado[0]][caminho_passado[1]]):
                posicao = [posicao[0], posicao[1]+1]
            elif (posicao[1]-1 >= 0 and (mapa[posicao[0]][posicao[1]-1] == "1" or mapa[posicao[0]][posicao[1]-1] == "3")
            and mapa[posicao[0]][posicao[1]-1] != mapa[caminho_passado[0]][caminho_passado[1]]):
                posicao = [posicao[0], posicao[1]-1]

            caminho_passado = temp

            if caminho_passado == posicao:
                d = False
            else:
                contador_passos += 1

            print(posicao, mapa[posicao[0]][posicao[1]])
            if mapa[posicao[0]][posicao[1]] == "3":
                c = False
                d = False
                print(contador_passos)


N, M = map(int, input().split())
contador_caminhos = 0
caminho_possivel = []
mapa = []
possibilidades = []
for x in range(N):
    entrada = input().split()
    mapa.append(entrada)
# Encontra 2 (posição inicial):
for x in range(N):
    for y in range(M):
        if mapa[x][y] == "2":
            P_inicial = [x, y]

lookAround(P_inicial, caminho_possivel, mapa)
runner(caminho_possivel, contador_caminhos, P_inicial)