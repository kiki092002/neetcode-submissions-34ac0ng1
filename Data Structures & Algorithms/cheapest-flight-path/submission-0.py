class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj_list = defaultdict(list)

        for flight in flights:
            s,e,p = flight
            adj_list[s].append((e,p))

        print(adj_list)
        min_price = float('inf')
        
        q = deque([(src,0,0)]) # 0,0
        while q:
            
            node,price,stops = q.popleft()
            print(node)
            
            if stops >k +1:
                continue
            if node == dst:
                min_price = min(min_price,price)
            for nei,p in adj_list[node]:
                new_p = price +p
                
                q.append((nei,new_p,stops+1))

        return min_price if min_price !=float('inf')else -1