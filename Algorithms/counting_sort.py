'''
    Organiza um array usando o algoritmo counting sort.
    exemplo:
    2 6 1 9 9 2 1 1 10 2
'''
array = list(map(int, input().split()))
new_array = []
first = min(array)
last = max(array)
dict = {}
# Dictionary constructor:
for x in range(first, last+1):
    dict[x] = 0
for x in range(first, last+1):
    for y in range(len(array)):
        if x == array[y]:
            dict[x] += 1
print(dict)

# New array constructor:
for x in range(first, last+1):
    for y in range(dict[x]):
        new_array.append(x)
print(new_array)