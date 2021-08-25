from graph import DFSVisit, buildGraphFromFile
import matplotlib.pyplot as plt
def findAPath(G,s,t):
    parent = {s: None}
    DFSVisit(G, s, parent)
    return extractPath(t,parent)
def extractPath(t,parent):
    if t not in parent :
        return []
    else:
        L=[]
        i=t
        L.append(t)
        while i != None :
            L.append(parent[i])
            i=parent[i]
        L=L[:-1]
        L=L[::-1]
        return L
G = buildGraphFromFile("UndirectedGraph2.txt", undirected =True)
# UndirectedGraph2.txt is available in compressed folder associated with this assignment
plt.figure(2)
plt.clf()
G.draw()
print(findAPath(G,'A','F'))
print(findAPath(G,'A','I'))