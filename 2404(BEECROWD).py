class Grafo:
    def __init__(self, V):
        self.pai = list(range(V))
        self.G = []
        self.T = []
    
    def adiciona_aresta(self, u, v, w):
        self.G.append((w, (u,v)))
    
    def find_set(self, i):
        if i == self.pai[i]:
            return i
        else:
            self.pai[i] = self.find_set(self.pai[i]) #Compression
            return self.pai[i]
    
    def union_set(self, u, v):
        self.pai[u] = v
    
    def kruskal(self):
        self.G.sort() #Sort edges by weight in ascending order
        minST = 0
        for w, (u, v) in self.G:
            uRep = self.find_set(u)
            vRep = self.find_set(v)
            if uRep != vRep:
                self.T.append((w, (u,v))) #Add to the minumum spanning tree
                self.union_set(uRep,vRep)
                minST += w
        
        return minST
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    
    #Create a graph wit m vertices
    g = Grafo(m)
    
    for _ in range(m):
        x,y,c = map(int, input().split())
        g.adiciona_aresta(x,y,c)
    
    minST = g.kruskal()
    
    print(minST)