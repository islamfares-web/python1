def elementDistinctnessFast(L):
    s= L.copy()
    s.sort()
    q= len(L)
    found = True
    if q < 2:
        return True
    else:
        for i in range(q-1):
            if s[i] == s[i+1]:
                found = False
    return found


print(elementDistinctnessFast([1,2,5,10,3,31,32,33,37,50,250]))
print(elementDistinctnessFast([1,2]))
print(elementDistinctnessFast([1]))
print(elementDistinctnessFast([]))
print(elementDistinctnessFast([1,2,5,2,10]))
print(elementDistinctnessFast([10,1,2,10]))
print(elementDistinctnessFast([1,2,5,10,3,31,32,33,37,5,250]))
print(elementDistinctnessFast([2,2]))

