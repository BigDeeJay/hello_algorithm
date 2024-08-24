from collections import deque

def solution(numbers):
    dq = deque()
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)):
        while dq and numbers[dq[-1]] < numbers[i]:
            answer[dq.pop()] = numbers[i]
        dq.append(i)
    return answer