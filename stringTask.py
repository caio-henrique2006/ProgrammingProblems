a = input().lower()
result = ""

vogais = ["a", "e", "y", "i", "o", "u"]

for x in range(len(a)):
    if not (a[x] in vogais):
        result = result + "." + a[x]
print(result)