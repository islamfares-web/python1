n =input("Enter integers speerated by spaces:")
L1 = n.split()
for i in range(len(L1)):
    L1[i] = int(L1[i])

q =input("Enter integers speerated by spaces:")
L2 = q.split()
for i in range(len(L2)):
    L2[i] = int(L2[i])

if L2==L1:
    print("permutation")
else:
    if len(L1)!=len(L2):
        print("no permutation!")
    else:
        for i in range(len(L1)):
            per = False
            for j in range(len(L2)):
                if(L1[i]==L2[j]):
                    per = True
                    break
            if not per:
                break
if per== True:
    print("The lsits are permutable")
else:
    print("The lsits are not permutable")