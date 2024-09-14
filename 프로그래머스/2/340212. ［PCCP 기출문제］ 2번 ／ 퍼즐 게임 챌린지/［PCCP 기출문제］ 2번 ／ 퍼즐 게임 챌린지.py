# 이분탐색
def solution(diffs, times, limit):
    low, high = 1, max(diffs)
    min_solved_time = pow(10, 15)
    
    if len(diffs) == 1:
        return 0
    
    while low <= high:
        level = (low + high) // 2
        calculated_time = calculate_solve_time(level, diffs, times)
        
        print(f'calculated_time = {calculated_time}, limit = {limit}, level = {level}, low = {low}, high = {high}')

        if calculated_time > limit: # 풀이시간 > limit => 숙련도 up
            low = level + 1
        else:
            high = level - 1
            min_solved_time = min(min_solved_time, level)
        
    return min_solved_time

def calculate_solve_time(level, diffs, times):
    total = 0
    
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        
        if diff <= level:
            total += time_cur
        else:
            time_prev = times[i - 1]
            total += (time_prev + time_cur) * (diff - level) + time_cur
            
    return total
        
    