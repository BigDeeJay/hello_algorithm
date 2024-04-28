from collections import deque

global arr;

def dfs(graph, key, prev, visited):
    global arr
    visited[key] = 1
    
    q = deque([key])
    
    while q:
        x = q.popleft()
        for node in graph[x]:
            if arr[node] == -1:
                q.append(node)
                arr[node] = arr[x] + 1

def solution(n, roads, sources, destination):
    answer = []
    global arr
    arr = [-1] * (n + 1)
    arr[destination] = 0
    
    graph = {}
    
    for road in roads:
        val1 = graph.get(road[0], [])
        val1.append(road[1])
        graph[road[0]] = val1
        
        val2 = graph.get(road[1], [])
        val2.append(road[0])
        graph[road[1]] = val2
        
    #print('graph', graph)
    
    visited = [0] * (n + 1)
    dfs(graph, destination, -1, visited)
    
    #print('arr', arr)
    
    for source in sources:
        if arr[source] == float('inf'):
            answer.append(-1)
        else:
            answer.append(arr[source])
            
    return answer