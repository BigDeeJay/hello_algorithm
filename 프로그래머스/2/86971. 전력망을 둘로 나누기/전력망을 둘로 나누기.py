edges = 0

def solution(n, wires):
    global edges
    graph = [[] for _ in range(n)]
    answer = 99_999
    # 그래프 그리기
    for wire in wires:
        x = wire[0] - 1
        y = wire[1] - 1

        graph[x].append(y)
        graph[y].append(x)
        
    for wire in wires:
        visited = [0] * n
        x = wire[0] - 1
        y = wire[1] - 1
        
        # 엣지 제거
        graph[x].remove(y)
        graph[y].remove(x)
        
        # 탐색
        edges = 1
        dfs(x, visited, graph)
        
        second_edges = n - edges
        result = abs(edges - second_edges)
        answer = min(answer, result)
        
        # 엣지 추가
        graph[x].append(y)
        graph[y].append(x)
        
    return answer

def dfs(start, visited, graph):
    global edges
    
    visited[start] = 1
    
    for node in graph[start]:
        if visited[node] == 0:
            dfs(node, visited, graph)
            edges += 1
    
    