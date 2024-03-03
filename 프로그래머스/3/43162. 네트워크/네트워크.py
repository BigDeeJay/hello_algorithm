def solution(n, computers):
    length = len(computers)
    graph = [[0 for _ in range(length)] for __ in range(length)]
    visited = [[0 for _ in range(length)] for __ in range(length)]
    net = [0] * n
    
    for i in range(length):
        com = computers[i]
        for j in range(length):
            if i == j or com[j] == 0:
                continue
            graph[i][j] = 1
    
    networks = 0
    for i in range(n):
        for j in range(n):
            if i == j or graph[i][j] == 0 or visited[i][j] == 1: continue
            # DFS를 통해 네트워크 그룹 탐색
            dfs(i, graph, visited, net)
            networks += 1

    sol = 0
    
    # 독립노드 체크
    for n in net:
        if n == 0: sol += 1
        
    # 네트워크 그룹 개수 + 독립노드 개수 = 정답
    return networks + sol

def dfs(j, graph, visited, net):
    node = graph[j]
    for k in range(len(node)):
        edge = node[k]
        if edge == 0 or visited[j][k] == 1: continue
        visited[j][k] = 1
        visited[k][j] = 1
        
        # 네트워크에 속한 노드 체크
        net[j] = 1
        net[k] = 1
        dfs(k, graph, visited, net)    