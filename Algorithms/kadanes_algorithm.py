'''
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