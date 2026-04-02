class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_list = self.get_adj_list(edges)
        count = 0

        def dfs(node,visited):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj_list[node]:
               
                dfs(nei,visited)
            return True 
        for node in range(n):
            if dfs(node,visited) == True:
                count+=1
        return count
    def get_adj_list(self,edges):
        res = defaultdict(list)
        for u,v in edges:
            res[u].append(v)
            res[v].append(u)

        return res