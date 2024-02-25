def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    dp = [[float("inf")] * 51 for _ in range(len(onboard))]
    
    adj_t1 = t1 + 10
    adj_t2 = t2 + 10
    adj_tmp = temperature + 10
    
    def_min_tmp = 0
    def_max_tmp = 51
    
    dp[0][adj_tmp] = 0
    
    # minute
    for m in range(1, len(onboard)):
        isOnboard = onboard[m]
            
        min_tmp = 0
        max_tmp = 0
        
        if isOnboard:
            min_tmp = adj_t1
            max_tmp = adj_t2 + 1
        else: 
            min_tmp = def_min_tmp
            max_tmp = def_max_tmp
            
        for tmp in range(min_tmp, max_tmp):
            lst = []
            # 실내온도 > 실외온도
            if tmp > adj_tmp:
                lst.append(dp[m - 1][tmp] + b) # 희망온도 & 현재기온 유지
                if tmp > def_min_tmp: lst.append(dp[m - 1][tmp - 1] + a) # 온도를 높이는데 a, 낮추는데 0
                if tmp < def_max_tmp - 1: lst.append(dp[m - 1][tmp + 1])
            # 실내온도 < 실외온도
            elif tmp < adj_tmp:
                lst.append(dp[m - 1][tmp] + b) # 희망온도 & 현재기온 유지
                if tmp > def_min_tmp: lst.append(dp[m - 1][tmp - 1]) # 온도를 높이는데 0, 낮추는데 a
                if tmp < def_max_tmp - 1: lst.append(dp[m - 1][tmp + 1] + a)
            elif tmp == adj_tmp:
                lst.append(dp[m - 1][tmp]) # 온도를 높이고 낮추는데 0
                if tmp > def_min_tmp: lst.append(dp[m - 1][tmp - 1])
                if tmp < def_max_tmp - 1: lst.append(dp[m - 1][tmp + 1])
            dp[m][tmp] = min(lst)
            
    return min(dp[len(onboard) - 1])