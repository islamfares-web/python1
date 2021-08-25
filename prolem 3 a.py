t = input("enter integers sperated by spaces:")
L = t.split()
maxsum = 0

for x in range(len(L)):
    L[x] = int(L[x])
for i in range(len(L)):
    for j in range(i,len(L)):
        a =0
        b =''
        for x in range (i,j+1):
            a += L[x]
            b += str(L[x])
        if a > maxsum:
            maxsum = a
            maxseries =b

print(maxsum)
print(maxseries)
