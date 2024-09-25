from collections import deque
from collections import defaultdict

def solution(points, routes):
    answer = 0
    rows, cols = 0, 0
    for point in points:
        rows = max(rows, point[0])
        cols = max(cols, point[1])
        
    grid = [[0] * cols for _ in range(rows)]
    
    for point in points:
        grid[point[0] - 1][point[1] - 1] = 1
    
    all_paths = []
    for route in routes:
        # continuous_paths = []
        # for i in range(len(route)):
        #     if i + 1 < len(route):
        #         continuous_paths += bfs_y_priority(grid, [route[i], route[i + 1]], points)
        # all_paths.append(continuous_paths)
        all_paths.append(min_route(route, points))
    # print('all_paths', all_paths)
    answer = overlap_count(all_paths)
        
    return answer

def overlap_count(all_paths):
    result_count = 0
    max_path_length = max(len(path) for path in all_paths)
    
    for i in range(max_path_length):
        count_dict = defaultdict(int)
        
        for path in all_paths:
            if i >= len(path):
                continue
            count_dict[path[i]] += 1
            
        for key, count in count_dict.items():
            if count > 1:
                result_count += 1
                
    return result_count
                
def min_route(route, points):
    # 경로를 저장할 path, 시간을 기록할 time
    path = []
    time = 0

    # 시작점과 도착점을 모두 탐색합니다.
    for i in range(len(route) - 1):
        # 시작점 sx, sy, 도착점 ex, ey
        sx, sy = points[route[i] - 1]
        ex, ey = points[route[i + 1] - 1]

        # x 좌표의 이동을 먼저 시작합니다.
        while sx != ex:
            # 시작점을 포함합니다.
            path.append((sx, sy, time))
            if sx > ex:
                sx -= 1
            else:
                sx += 1
            time += 1

        # y 좌표를 이동합니다.
        while sy != ey:
            # x 좌표가 이동이 끝났을 때 값을 추가합니다.
            path.append((sx, sy, time))
            if sy > ey:
                sy -= 1
            else:
                sy += 1
            time += 1

    # 최종적으로 도착점에 도착했을 때만 마지막으로 추가해줍니다.
    path.append((sx, sy, time))
    # 경로를 반환합니다.
    return path
    
def bfs_y_priority(grid, route, points):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    start = points[route[0] - 1]
    end = points[route[1] - 1]

    dq = deque([((start[0] - 1, start[1] - 1), [(start[0] - 1, start[1] - 1)])])

    visited[start[0] - 1][start[1] - 1] = True
    result_paths = []
    
    while dq:
        (x, y), paths = dq.popleft()
        
        if (x, y) == (end[0] - 1, end[1] - 1):
            result_paths = paths
            continue
                        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if (0 <= nx < rows and 
                0 <= ny < cols and 
                not visited[nx][ny] and 
                ((nx, ny) == (end[0] - 1, end[1] - 1) or grid[nx][ny] == 0)):
                    
                visited[nx][ny] = True
                dq.append(((nx, ny), paths + [(nx, ny)]))
                
    return result_paths
            
    