def indexOfmin(L,start,end):
    if start <= end and end <= len(L):
        ind = start
        minimum=L[start]
        
        for i in range(start+1,end+1):
            if L[i] < minimum:
                minimum = L[i]
                ind = i
        return ind

def slectionSort(L):
    for i in range (len(L)):
        k = indexOfmin(L,i,len(L)-1)
        (L[i], L[k]) = (L[k], L[i])
    return L

print(slectionSort([5,6,8,2,4,6]))
