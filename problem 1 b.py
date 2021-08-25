from graph import UndirectedGraph
def check_if_adjacent(M,i,j):
    O=len(M)
    N=len(M[0])
    L=[]
    if i< O-1 and M[i+1][j]:
        L.append((i+1,j))
    if j< N-1 and M[i][j+1]:
        L.append((i,j+1))
    if i>0 and M[i-1][j]:
        L.append((i-1,j))
    if j>0 and M[i][j-1]:
        L.append((i,j-1))
    return L

def buildGraphFromMaze(M):
    G = UndirectedGraph()
    for i in range (len(M)):
        for j in range (len(M[0])):
            if M[i][j] == True:
                G.addNode((i,j))
    for i in range (len(M)):
        for j in range (len(M[0])):
            if M[i][j] == True:
                for (x,z) in check_if_adjacent(M,i,j):
                    if (i <=x or j<=z) and not ((i,j) in G.adj[(x,z)]):
                        G.connect((i,j),(x,z))

    return G
import numpy
M = [[True, False, True],
[True, True, True],
[True, False, True]]
print("M:")
print(numpy.matrix(M,int))
G= buildGraphFromMaze(M)
print("G:")
print(G)