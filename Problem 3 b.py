def modeSearch (okay):
    first = 0
    last = len(okay)-1
    mode = 0
    found = False
    while first <=last and not found:
        mid = (first + last)//2
        if mid == first or mid ==last:

            found = True
        elif okay[mid] < okay[mid - 1]:
            last = mid
            mode = last
            if mode == first:

                found = True
            else:
                if okay[mode] < okay[mode -1]:
                    mode -=1
                else:
                    found = True
        else:
            first = mid
            mode= first
            if mode == last:
                found = True
            else:
                if okay[mode] < okay[mode+1]:
                    mode += 1
                else:
                    found = True
    return mode
L = [1,2,5,20]
print(modeSearch(L))



