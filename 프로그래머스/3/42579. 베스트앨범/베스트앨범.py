def solution(genres, plays):
    answer = []
    dt = {}
    idxs = {}
    
    leng = len(genres)
    
    for i in range(leng):
        genre = genres[i]
        play = plays[i]
        
        val = dt.get(genre, 0)
        dt[genre] = val + play
        
        valval = idxs.get(genre, [])
        valval.append({
            'idx': i,
            'play': play
        })
        idxs[genre] = valval
    
    dt = sorted(dt.items(), key = lambda item : -item[1])
    # print('dt', dt)
    # print('idxs', idxs)
    
    for data in dt:
        #print('genre', genre)
        ranks = idxs[data[0]]
        ranks.sort(key = lambda x : (-x['play'], x['idx']))
        cnt = 0
        
        # print('ranks', ranks)
        
        ranks_len = len(ranks)
        
        if ranks_len == 1:
            answer.append(ranks[0]['idx'])
        else:
            for i in range(2):
                answer.append(ranks[i]['idx'])
                
    return answer