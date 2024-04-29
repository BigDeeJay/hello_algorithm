from collections import deque

def solution(x, y, n):
    MAX_VAL = 1_000_001
    dp = [10_000] * MAX_VAL
    dp[x] = 0
    
    for i in range(x, MAX_VAL):
        if dp[x] == 10_000:
            continue
            
        if i + n < MAX_VAL:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
            
        if i * 2 < MAX_VAL:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
            
        if i * 3 < MAX_VAL:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
            
    if dp[y] == 10_000:
        return -1
    
    return dp[y]