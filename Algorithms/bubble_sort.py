'''
    Organizar uma lista de números usando o algoritmo bubble(sort).
    exemplo:
    3 4 5 1 2 9 7
'''
array = list(input().split())
condition = True
while condition:
    condition = False
    for y in range(len(array)-1):
        if int(array[y]) > int(array[y+1]):
            keeper = array[y]
            array[y] = array[y+1]
            array[y+1] = keeper
            condition = True
print(array)
