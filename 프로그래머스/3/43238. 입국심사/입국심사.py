def solution(n, times):
    answer = 0
    left = 1
    right = 1_000_000_000_000 * 1_000_000_000_000
    
    while left <= right:
        mid = left + (right - left) // 2
        total = 0
        # total: 해당시간 동안 처리가능한 인원
        for time in times:
            total += mid // time
            
        # mid 시간 내에 모든 인원이 처리가능한 경우
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    #print('answer', answer)
    
    return answer