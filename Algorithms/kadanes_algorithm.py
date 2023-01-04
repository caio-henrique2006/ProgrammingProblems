'''
    Descobre a maior soma consecutiva dentro de um array com números negativos:
    Exemplo:
    2 -1 3 4 -4 -6 1 2
'''
array = list(input().split())
max_ate_agora = 0
max_final = 0
for x in range(len(array)):
    max_final = max_final + int(array[x])
    if max_final < 0:
        max_final = 0
    if max_final > max_ate_agora:
        max_ate_agora = max_final
print(max_ate_agora)