from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    graph = defaultdict(lambda: [0, 0])
    
    for s, e in edges:
        graph[s][1] += 1
        graph[e][0] += 1
        
    for items in graph.items():
        node, num = items
        
        if num[0] == 0 and num[1] >= 2:
            answer[0] = node
        elif num[0] >= 2 and num[1] >= 2:
            answer[3] += 1
        elif num[0] > 0 and num[1] == 0:
            answer[2] += 1
    
    # 시작정점에서 뻗어나간 간선의 개수 = 총 그래프 개수
    donut = graph[answer[0]][1] - answer[2] - answer[3]
    answer[1] = donut
    
    return answer