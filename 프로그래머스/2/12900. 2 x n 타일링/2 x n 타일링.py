def solution(n):
    answer = 0
    
    # n = 1 -> 1 (1)
    # n = 2 -> 2 (1)
    # n = 3 -> 3 (0)
    
    # n = 4 -> f(3) * 1 + f(2) * 1 + f(1) * 0
    # n = 5 -> f(4) * 1 + f(3) * 1 + f(2) * 0 + f(1) * 1
    # n = 6 -> f(5) * 1 + f(4) * 1 + f(3) * 0 + f(2) * 1 + f(1) * 0
    
    # f(n) = f(n - 3) + f(n - 4) + f(n - 5) + f(n - 6) + f(n - 2)
    # n = 6 (1)
    
    # [0, 1, 1, 0, 0, 0, 1, 0, 1]
    
    dp = [0, 1, 2, 3]
    pattern = [0, 1, 1, 0, 1, 0]
    isZero = True
    
    for i in range(4, n + 6):
        # val = 0
        # for j in range(1, i):
        #     val += dp[i - j] * pattern[j]
        # dp.append(val % 1_000_000_007)
        # if isZero:
        #     pattern.append(0)
        #     isZero = False
        # else :
        #     pattern.append(1)
        #     isZero = True
        
         # f(n) = f(n - 3) + f(n - 4) + f(n - 5) + f(n - 6) + f(n - 2)
        #val = (dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6] + dp[i - 2]) % 1_000_000_007
        
        val = (dp[i - 1] + dp[i - 2]) % 1_000_000_007
        dp.append(val)
            
    # print('dp', dp)
    return dp[n]