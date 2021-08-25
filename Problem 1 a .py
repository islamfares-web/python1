def f(n):
    global N
    N += 1
    if n==0 or n==1 or n==2:
        return 1
    else:
        return f(n - 1) + f(n - 2) + f(n - 3) + f(n//3)
z=int(input("Enter range of n between zero and ...:"))
for i in range(z):
    N=0
    print(f(i), end=" ")
N = 0
s=int(input("\nEnter an integer:"))
print(f(s))
print("number of repetitions",N)
