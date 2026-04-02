class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        def bfs(u,v):
            visit=set()
            q = deque([u])
            visit.add(u)
            while q:
                node = q.popleft()
                if node == v:
                    return True
                for nei in graph[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            return False
        for u,v in edges:
            if bfs(u,v):
                return [u,v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        
        



        
                    