def f(n):
    if n < 2:
        L = [1] *(n+1)
    else:
        L=[1,1,1]
        for i in range (3,n+1,1):
            L.append(L[i-1]+L[i-2]+L[i-3] +L[i//3]+3)

    return L[n]

for i in range(10):
    print(f(i), end=" ")

n=int(input("\nEnter an integer:"))
print("\nf(25): ",f(n))
