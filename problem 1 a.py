from graph import UndirectedGraph
import matplotlib.pyplot as plt


def buildCircleGraph(n):
    G = UndirectedGraph()
    assert n > 2, "The entered integer should be 3 and above"
    for i in range(n):
        G.addNode(i)
    for i in range(n-1) :
        G.connect(i,i+1)
    G.connect(n-1,0)
    return G
g= buildCircleGraph(5)
print(g)
plt.figure(1)
plt.clf()
g.draw()