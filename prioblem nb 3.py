def f(x):
    assert type(x) == int and n > 0;
    "bad input!!!"
    if n <= 3:
        return 2  # base case
    else:
        return 2 * f(x - 1) + f(x - 2)  # reccursion
def file1(filename):
    NH1=open('filename', 'w')
    for i in range 21:
        NH1.write('x/t')
        NH1.write('f(x)/n')
        NH1.write(i,'/t')
        NH1.write(f(i),'n')
    NH1.close
file1(output.txt)

import matplot.pyplot as plt
def readFileAndPLot(filename):
    namehandle = open("output.txt".'r')
    for line in namehandle:
        plt.plot(line,"r")
        plt.xlabel(“x”)
        plt.ylabel(“F(x)”)
        plt.title( “Recursion Fig. 1”)
    namehandle.close()