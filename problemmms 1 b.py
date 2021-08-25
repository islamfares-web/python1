def f(n):
    def f(n,L):
        global N
        N += 1
        if L[n] != -1:
            return L[n]
        elif n==0 or n==1 or n==2:
            L[n]=1

        else:
            L[n]= f(n - 1,L) + f(n - 2,L) + f(n - 3,L) + f(n//3,L)
        return L[n]
    L = [-1]*(n+1)
    return f(n,L)
'''z=int(input("Enter range of n between zero and ...:"))
for i in range(z):
    N=0
    print(f(i), end=" ")'''
N = 0
s=int(input("\nEnter an integer:"))
print(f(s))
print("number of repetitions",N)