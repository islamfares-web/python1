def search(okay, mode):
    def modeSearchrecusrive(okay, mode, first, last):
        if first > last:
            return -1
        mid = (first + last) // 2
        if okay[mid] == mode:
            return mid
        elif okay[mid] < mode:
            return modeSearchrecusrive(okay, mode, mid + 1, last)
        else:
            return modeSearchrecusrive(okay, mode, first, mid - 1)

    return modeSearchrecusrive(okay, mode, 0, len(okay) - 1)
def secondWAy(L, low, high):
    m= (low + high)//2
    if m <= len(L)-2 and L[m] < L[m+1]:#this way searching for max directly in binary search..
        return secondWAy(L, m+1, high)
    elif m >= 1 and L[m] < L[m-1]:
        return secondWAy(L, low, m-1)
    else:#if m <1 return it and if greater than len(L)-2 (minus 2 b ecause we have two terms m and m+1 not to get list out of range) or if its max
        return m
