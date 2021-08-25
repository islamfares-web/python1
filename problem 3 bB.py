t = input("enter integers sperated by spaces:")
L = t.split()
maxsum = 0

for x in range(len(L)):
    L[x] = int(L[x])
for i in range(len(L)):
    for j in range(i,len(L)):
       Lh= L[i:j+1:1]
       a = sum(Lh)
        if a > maxsum:
            maxsum = a
            maxseries =""
            for x in Lh:
                maxseries+=str(x)

print(maxsum)
print(maxseries)
