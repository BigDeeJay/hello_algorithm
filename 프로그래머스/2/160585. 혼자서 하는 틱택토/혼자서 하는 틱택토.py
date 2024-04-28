oTic = 0
xTic = 0

def solution(board):
    answer = -1
    
    xCnt = 0
    oCnt = 0

    def checkTic(s):
        global oTic
        global xTic
        
        if s == 'OOO':
            oTic += 1
        elif s == 'XXX':
            xTic += 1
    
    for i in range(0, 3):
        print(i, board[i])
        checkTic(board[i])
        vertical = board[0][i] + board[1][i] + board[2][i]
        checkTic(vertical)
        
        for j in board[i]:
            if j == 'O':
                oCnt += 1
            elif j == 'X':
                xCnt += 1

    down = board[0][0] + board[1][1] + board[2][2]
    up = board[0][2] + board[1][1] + board[2][0]
    
    print(down)
    print(up)
    
    print('xCnt = ' + str(xCnt) + ', oCnt = ' + str(oCnt))
    
    checkTic(down)
    checkTic(up)
    
    # X의 갯수가 O보다 많을 수 없음
    # 모든 칸이 차 있으면 진행불가
    if xCnt > oCnt or abs(oCnt - xCnt) > 1:
        return 0
    
    # 일치된 틱택토가 2개 이상이면 틀림
    if xTic > 0 and oTic > 0:
        return 0
    
    if xTic > 0 and (xCnt != oCnt):
        return 0
    
    if oTic > 0 and (xCnt + 1 != oCnt):
        return 0
    
    return 1