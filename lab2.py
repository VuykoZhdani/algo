from collections import defaultdict
class Graph:
    def __init__(self, curVertices):
        self.curV = curVertices 

        self.graph = defaultdict(list) 

    def addEdge(self, curV, w):
        self.graph[curV].append(w)
        self.graph[w].append(curV)
    def isCyclicUtil(self, curV, visited, parent):
        visited[curV] = True
        for i in self.graph[curV]:
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, curV)):
                    return True
            elif parent != i:
                return True
 
        return False
    def isCyclic(self):
        visited = [False]*(self.curV)
        for i in range(self.curV):
            if visited[i] == False:
                if(self.isCyclicUtil
                   (i, visited, -1)) == True:
                    return True
 
        return False
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
if g.isCyclic():
    file1 = open("dodik.txt","w")
    L = ["Durachok has a cycle and woolf sends his bests\nTrue"] 
    file1.writelines(L)
    file1.close()
else:
    file1 = open("dodik.txt","w")
    L = ["Where the fuck is my cycle???????\nFalse"] 
    file1.writelines(L)
    file1.close()
