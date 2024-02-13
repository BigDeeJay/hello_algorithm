def solution(coin, cards):
    answer = 0
    n = len(cards)
    target = n + 1
    # print(target)
    myCard = {}
    for i in range(n // 3):
        myCard[cards.pop(0)] = 1
    all_round = len(cards) // 2
    temp = {}
    nowRound = 1
    for i in range(all_round):
        temp[cards.pop(0)] = 1
        temp[cards.pop(0)] = 1
        
        #print('myCard = ', myCard)
        #print('temp = ', temp)
        #print('coin = ', coin)
        #print('card = ', cards)
        
        check = False

        for key in myCard.copy():
            reverse = target - key
            if myCard.get(reverse) != None:
                del myCard[reverse]
                del myCard[key]
                check = True
                nowRound += 1
                break
                
        if coin > 0 and check == False:
            for key in myCard.copy():
                reverse = target - key
                if coin > 0 and temp.get(reverse) != None:
                    del temp[reverse]
                    del myCard[key]
                    check = True
                    nowRound += 1
                    coin -= 1
                    break
                
        if coin > 1 and check == False:
            for key in temp.copy():
                reverse = target - key
                if temp.get(reverse) != None:
                    del temp[key]
                    del temp[reverse]
                    coin -= 2
                    nowRound += 1
                    check = True
                    break
                    
        if check == False:
            break
    return nowRound