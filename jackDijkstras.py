import time
from prettytable import PrettyTable

class Graph:
    def __init__(self, totalNodes):
        self.totalNodes = totalNodes
        self.edges = [[-1 for i in range(totalNodes)] for j in range(totalNodes)]
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstras(self, start):
        distances = {n:float("inf") for n in range(self.totalNodes)}
        distances[start] = 0
        previousVertex = [0 for n in range(self.totalNodes)]
        for currentVertex in range(0,self.totalNodes,1):
            for neighbor in range(0,len(self.edges[currentVertex]),1):
                if(self.edges[currentVertex][neighbor] == -1):
                    continue
                elif distances[neighbor] == float("inf"):
                    distances[neighbor] = self.edges[currentVertex][neighbor]+distances[currentVertex]
                    previousVertex[neighbor] = currentVertex
                elif (self.edges[currentVertex][neighbor] + distances[currentVertex]) < distances[neighbor]:
                    distances[neighbor] = self.edges[currentVertex][neighbor] + distances[currentVertex]
                    previousVertex[neighbor] = currentVertex

        #CODE TO PRINT A PRETTY TABLE OF THE NODES AND THEIR SHORTEST DISTANCES, AND SHORTEST PATH TO FOLLOW BACK TO START
        #     print(self.edges[currentVertex])
        #     print(distances)
        #     print() 
        # print(previousVertex)
        # x = PrettyTable()
        # x.field_names = ["Node", "Distance From Node " + str(start+1), "Previous Node"]

        # for vertex in range(len(distances)):
        #     if(vertex==4):
        #         bDistance = distances[vertex]
        #     x.add_row([vertex, distances[vertex], previousVertex[vertex]])
        #     x.add_row(["", "",""])
        # print(x)
        # print("\n\nShortest Distance from node a to b = " + str(bDistance))


g=  Graph(6)

g.add_edge(0,5,14)
g.add_edge(0,1,7)
g.add_edge(0,2,9)
g.add_edge(1,2,10)
g.add_edge(1,3,15)
g.add_edge(2,3,11)
g.add_edge(2,5,2)
g.add_edge(3,4,6)
g.add_edge(4,5,9)


g.dijkstras(0)