x=input("Enter a string:")
olline= True
for i in range ((len(x)-1)//2):
    if x[i]!=x[len(x)-1-i]:
        olline= False
        break
print (olline)
            