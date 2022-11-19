n = int(input())
total = 0
for x in range(n):
    a = input()
    print(int(a))
    soma = 0
    for y in range(len(a)):
        soma += int(a[y])
    if soma >= 2:
        total += 1
print(total)
