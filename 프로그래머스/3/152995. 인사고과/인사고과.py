def solution(scores):
    answer = 1
    wanho = scores[0]
    rs = sorted(scores, key = lambda x: (-x[0], x[1]))
    maxB = 0
    
    # print('rs', rs)
    
    for score in rs:
        if (score[0] > wanho[0] and score[1] > wanho[1]):
            return -1
        
        if score[1] >= maxB:
            # print("maxB", maxB)
            maxB = score[1]
            
            if wanho[0] + wanho[1] < score[0] + score[1]:
                answer += 1
    return answer