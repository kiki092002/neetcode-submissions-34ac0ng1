class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u,v in edges:
            if uf.connected(u,v):
                return [u,v]
            else:
                uf.union(u,v)
        return []



class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False          # already connected

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True  
    def connected(self,x,y):
        return self.find(x) == self.find(y)