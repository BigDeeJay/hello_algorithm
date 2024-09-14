from collections import deque

def solution(game_board, table):
    answer = 0
    board_pieces = find_pieces(game_board, 0)
    table_pieces = find_pieces(table, 1)
            
    for blank in reversed(board_pieces):
        for puzzle in reversed(table_pieces):
            is_equal_matrix = False
            
            rotated_puzzle = puzzle
            
            for _ in range(4):
                # print('rotated_puzzle', rotated_puzzle)
                if blank == rotated_puzzle:
                    is_equal_matrix = True
                    break
                rotated_puzzle = rotate_matrix(rotated_puzzle)
            # print('----------')
                
            if is_equal_matrix:
                answer += count_matrix_point(puzzle)
                table_pieces.remove(puzzle)
                board_pieces.remove(blank)
                # print(f'puzzle = {puzzle}, blank = {blank}')
                break
                
    return answer
                
def count_matrix_point(matrix):
    # print('matrix', matrix)
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += 1
                
    return count
            
def rotate_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # 회전된 매트릭스의 새로운 크기
    new_matrix = [[0] * num_rows for _ in range(num_cols)]

    # 원본 매트릭스의 각 요소를 회전된 매트릭스에 배치
    for i in range(num_rows):
        for j in range(num_cols):
            new_matrix[j][num_rows - 1 - i] = matrix[i][j]
    
    return new_matrix

def compare_matrix(matrix1, matrix2):
    if (len(matrix1) != len(matrix2)
        or len(matrix1[0]) != len(matrix2[0])):
        return False
    
    N = len(matrix1)
    
    for i in range(N):
        for j in range(N):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    
    return True

def normalize_coords(coords):
    min_x = min(x for x, y in coords)
    min_y = min(y for x, y in coords)
    return [(y - min_y, x - min_x) for x, y in coords]

def create_matrix(nomalized_coords):
    max_x = max(x for x, y in nomalized_coords)
    max_y = max(y for x, y in nomalized_coords)
    
    matrix = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    
    for coords in nomalized_coords:
        matrix[coords[1]][coords[0]] = 1

    return matrix
    
def find_pieces(matrix, target_value):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    collected_pieces = []
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == target_value and not visited[row][col]:
                collected_pieces.append(create_matrix(normalize_coords(bfs(matrix, row, col, visited, target_value))))
    
    return collected_pieces
                
def bfs(matrix, start_row, start_col, visited, target_value):
    rows = len(matrix)
    cols = len(matrix[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dq = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    pieces = []
    
    while dq:
        row, col = dq.popleft()
        pieces.append((row, col))
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows 
                and 0 <= new_col < cols
                and matrix[new_row][new_col] == target_value
                and not visited[new_row][new_col]):
                    visited[new_row][new_col] = True
                    dq.append((new_row, new_col))
    return pieces