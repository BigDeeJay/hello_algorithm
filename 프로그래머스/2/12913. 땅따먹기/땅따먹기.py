def getValue(prevRow, currentValue, blockedIndex):
    # 이전에 사용한 인덱스 외 모든 경우의 수 비교
    maxValue = -1
    #print('prevRow', prevRow)
    for i in range(len(prevRow)):
        if i == blockedIndex:
            continue
        prevValue = prevRow[i]
        maxValue = max(maxValue, prevValue + currentValue)
    return maxValue

def solution(land):
    answer = 0
    for i in range(1, len(land)):
        currentRow = land[i]
        # print('currentRow', currentRow)
        for j in range(len(currentRow)):
            # 계산된 최대값으로 현재값 교체
            land[i][j] = getValue(land[i - 1], currentRow[j], j)
    #print('land', land)
    return max(land[len(land) - 1])