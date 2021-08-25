def power2(s):
    return s*s

def recPowerFast(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        if n%2 != 0:
            return 1/(x*recPowerFast(x, ((-n+1)/2))*recPowerFast(x, ((-n+1)/2)))
        else:
            return 1 / (recPowerFast(x,((-n)//2)) *recPowerFast(x, ((-n)//2)))
    else:
        if n % 2 != 0:
            return recPowerFast(x, 1)*recPowerFast(x, ((n-1)/2))*recPowerFast(x, ((n-1)/2))
        else:
            return recPowerFast(x,(n//2)) *recPowerFast(x, (n//2))



print("recPowerfast(0,0):",recPowerFast(9,3))
print("recPowerfast(0,3):",recPowerFast(0,3))
print("recPowerfast(3,0):",recPowerFast(3,0))
print("recPowerfast(3,1):",recPowerFast(3,1))
print("recPowerfast(-3,1):",recPowerFast(-3,1))
print("recPowerfast(2,4):",recPowerFast(2,4))
print("recPowerfast(2,-4):",recPowerFast(2,-4))