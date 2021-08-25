def recPowerSlow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return 1/(x * recPowerSlow(x, (-n) - 1))
    else:
        return x*recPowerSlow(x, n-1)

print("recPowerSlow(0,0):",recPowerSlow(0,0))
print("recPowerSlow(0,3):",recPowerSlow(0,3))
print("recPowerSlow(3,0):",recPowerSlow(3,0))
print("recPowerSlow(3,1):",recPowerSlow(3,1))
print("recPowerSlow(-3,1):",recPowerSlow(-3,1))
print("recPowerSlow(2,4):",recPowerSlow(2,4))
print("recPowerSlow(2,-4):",recPowerSlow(2,-4))
x = 1.25
n = 82
d=print(x,"**",n," :",x**n)
c=print("recPower(",x,",",n,"):",recPowerSlow(x,n))

if c==d:
    print("Correct")
else:
    print("Wrong")
