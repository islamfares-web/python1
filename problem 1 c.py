from graph import DiGraph, buildGraphFromFile
import matplotlib.pyplot as plt

def transpose (G):
    G_test=DiGraph()
    for i in G.adj:
        G_test.addNode(i)
    for i in G.adj:
        for j in G.adj[i]:
            G_test.connect(j,i)
    return G_test

G = buildGraphFromFile("DiGraph1.txt", undirected = False)
# DiGraph1.txt is available in compressed folder associated with this assignment
plt.figure(1)
plt.clf()
G.draw()
GTranspose = transpose(G)
plt.figure(2)
plt.clf()
GTranspose.draw()



