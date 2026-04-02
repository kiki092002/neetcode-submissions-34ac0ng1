class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #no cycle exactly n-1 edges for n nodes
        # all nodes connected 
        if len(edges)!=n-1:
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit = set()
        def dfs(node,parent):
            visit.add(node)

            for nei in graph[node]:
                if nei not in visit:
                    if dfs(nei,node):
                        return True
                elif nei != parent:
                    return True # cycle found
            return False
        if dfs(0,-1):
            return False
        return len(visit) == n