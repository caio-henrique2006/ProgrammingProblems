
n = input()
cond1 = False

div = [4, 7, 44, 47, 74, 77, 444, 447, 477]

# Lucky number:
for x in n:
    cond1 = True
    if x != "7" and x != "4":
        cond1 = False
        break
for x in range(len(div)):
    if int(n) % div[x] == 0:
        cond1 = True

if cond1:
    print("YES")
else:
    print("NO")