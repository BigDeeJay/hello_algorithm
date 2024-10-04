from collections import deque

def solution(A, B):
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    dq_B = deque(B)
    
    count = 0
    for a in A:
        while dq_B:
            b_value = dq_B.popleft()
            
            if b_value > a:
                count += 1
            else:
                dq_B.appendleft(b_value)
                
            break            
    
    return count