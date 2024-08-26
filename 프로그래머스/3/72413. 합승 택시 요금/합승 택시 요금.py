import heapq # 우선순위큐
from math import inf

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for start, end, cost in fares:  # 각 노드와 연결된 edge 체크
        graph[start].append([end, cost])
        graph[end].append([start, cost])
                
    def dijkstra(start, end):
        dist = [inf] * (n + 1)
        
        dist[start] = 0
        q = []
        heapq.heappush(q, [0, start])
        
        while q:
            d, cur = heapq.heappop(q)
            if dist[cur] < d:
                continue  
            for edge in graph[cur]:
                cost = d + edge[1] 
                
                if cost < dist[edge[0]]:
                    dist[edge[0]] = cost
                    heapq.heappush(q, [cost, edge[0]])
                    
        return dist[end]
    
    # 처음부터 각자 택시를 타고 목적지로 이동
    res = dijkstra(s, a) + dijkstra(s, b)
    for via in range(1, n + 1):
        if via == s:
            continue
        # 목적지로 함께 이동 후 각자 장소로 이동 cost 비교
        res = min(res, dijkstra(s, via) + dijkstra(via, a) + dijkstra(via, b)) 
    
    return res