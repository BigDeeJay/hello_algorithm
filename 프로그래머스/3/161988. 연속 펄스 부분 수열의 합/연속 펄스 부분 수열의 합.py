def solution(sequence):
    answer = 0
    p1 = []
    p2 = []
    val = 1
    
    for i, s in enumerate(sequence):
        p1.append(val * s) # 1로 시작하는 시퀀스
        p2.append(-val * s) # -1로 시작하는 시퀀스
        val = val * -1
        
    p1MaxSum = calculateMaxSum(p1)
    p2MaxSum = calculateMaxSum(p2)
    
    print(f'p1MaxSum = {p1MaxSum}, p2MaxSum = {p2MaxSum}')
    return max(p1MaxSum, p2MaxSum)

def calculateMaxSum(arr):
    maxVal = 0
    summ = 0
    
    for i in range(len(arr)):
        nowVal = arr[i]
        summ = summ + nowVal
        if summ < 0:
            summ = 0
        maxVal = max(maxVal, summ)
        
    return maxVal 