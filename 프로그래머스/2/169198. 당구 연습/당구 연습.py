def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:    
        arr = []
        
        if (startY != ball[1] or startX > ball[0]):
            arr.append(calcDistance([startX + (m - startX) * 2, startY], ball))
        
        if (startY != ball[1] or startX < ball[0]):
            arr.append(calcDistance([-startX, startY], ball))

        if (startX != ball[0] or startY > ball[1]):
            arr.append(calcDistance([startX, startY + (n - startY) * 2], ball))
            
        if (startX != ball[0] or startY < ball[1]):
            arr.append(calcDistance([startX, -startY], ball))
            
        answer.append(min(arr))
    return answer

def calcDistance(a, b):
    return pow(abs(a[0] - b[0]), 2) + pow(abs(a[1] - b[1]), 2)