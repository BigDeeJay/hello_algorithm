fields = []
answer = 0
min_cost = 0

def solution(m, n, puddles):
    global fields
    global answer
    global min_cost
    MOD = 1_000_000_007
    
    fields = [[0 for _ in range(m)] for __ in range(n)]
    fields[0][0] = 1
    for p in puddles:
        fields[p[1] - 1][p[0] - 1] = -999 # 웅덩이 표시
        
    for i in range(n):
        for j in range(m):
            # print(f'i : {i}, j : {j}, value : {now_cost}')
            
            if fields[i][j] == -999:
                continue
            
            # 오른쪽
            if j - 1 >= 0 and fields[i][j - 1] != -999:
                fields[i][j] += fields[i][j - 1] 
            # 아래
            if i - 1 >= 0 and fields[i - 1][j] != -999:
                fields[i][j] += fields[i - 1][j]
                
    print(f'필드 : {fields}')
    return fields[n - 1][m - 1] % MOD