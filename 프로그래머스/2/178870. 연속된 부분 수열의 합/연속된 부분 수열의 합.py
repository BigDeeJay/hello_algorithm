def solution(sequence, k):
    # 투포인터
    s, f = 0, 0
    summ = sequence[0]
    answer = [0, len(sequence)] # answer 값 최대로 초기화
    
    while f < len(sequence):
        if summ < k:
            f += 1
            if f == len(sequence): break
            summ += sequence[f]
        else:
            if summ == k:
                if f - s < answer[1] - answer[0]: # 길이가 더 짧은 수열 찾기
                    answer = [s, f]
            summ -= sequence[s] # 늦은 포인터 올리기
            s += 1
            
    return answer