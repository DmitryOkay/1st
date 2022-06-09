#дан спісок, вывесті элементы которые встречаются одін раз!
A = ['b','b','c','d','e','e']
B = []
for i in A:
    if i not in B:
        B.append(i)
print(B)


