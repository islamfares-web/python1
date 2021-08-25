n =input("Enter integers speerated by spaces:")
l = n.split()
for i in range(len(l)):
    l[i] = int(l[i])
    decreasing = False
for i in range(1,len(l)):
    if l[i-1] > l[i]:
        decreasing = False
    else:
        decreasing = True
            
if decreasing == True:
    print('yes')
else:
    print("not")
    

    
    