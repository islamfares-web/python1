t = input("enter integers sperated by spaces:")
L = t.split()
maxsum = 0

for x in range(len(L)):
    L[x] = int(L[x])
for i in range(len(L)):
    a =0
    b =''
    for j in range(i,len(L)):
         a+=L[j]
         b+= str (L[j])
        if a > maxsum:
            maxsum = a
            maxseries =b

print(maxsum)
print(maxseries)
