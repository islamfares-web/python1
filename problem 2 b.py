from graph import buildGraphFromFile

import matplotlib.pyplot as plt
from circularQueue import Queue
import numpy
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

def BFS(G,s,t):
    assert s in G.adj, "node not on graph"
    parent ={s:None}
    distance={s:0}
    Q =Queue(len(G.adj))
    Q.enqueue(s)
    while not Q.isEmpty():
        u = Q.dequeue()
        for v in G.adj[u]:
            if v not in distance:
                distance[v]=distance[u]+1
                parent[v]=u
                Q.enqueue(v)

    return parent

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
def findshortestpath(G,s,t):
    parentt=BFS(G,s,t)
    return  extractPath(t,parentt)



G = buildGraphFromFile("UndirectedGraph2.txt", undirected =True)

plt.figure(2)
plt.clf()
G.draw()

print(findshortestpath(G,"A","F"))
print(findshortestpath(G,"A","I"))


M=[[True, False, True, True, False, True, True],
[True, True, False, True, True, False, False],
[False, True, True, True, True, True, True],
[False, True, True, False, False, False, True],
[False, True, False, True, True, False, True]]
print("M:")
print(numpy.matrix(M,int))
GMaze= buildGraphFromMaze(M)
print(findshortestpath(GMaze,(0,0),(4,6)))