# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:09:55 2018

@author: lb13
"""


from graph import buildGraphFromFile 
import matplotlib.pyplot as plt
G = buildGraphFromFile("DiGraph1.txt", undirected = False)
plt.figure()
#plt.clf()
G.draw()
#plt.clf()
#plt.plot([1,2],[2,3])

G = buildGraphFromFile("UndirectedGraph1.txt", undirected = True)
plt.figure(10)
plt.clf()
G.draw()