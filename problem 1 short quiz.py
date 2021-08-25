def f(x):
    assert type(x)== int and n >0; "bad input!!!"
    if n <=3:
        return 2 #base case
    else:
        return 2 * f(x-1) + f(x-2) # reccursion
    
