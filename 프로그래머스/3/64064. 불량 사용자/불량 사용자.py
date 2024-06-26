count = 0
result = set([])

def solution(user_id, banned_id):
    answer = 0
    max_depth = len(banned_id)
    combination([], 0, user_id, banned_id, max_depth)
    return len(result)

def combination(arr, depth, user_id, banned_id, max_depth):
    global result
    if depth == max_depth:
        if len(arr) == max_depth:
            arr.sort()
            result.add(tuple(arr))
        return
    
    for i in range(depth, len(banned_id)):
        bid = banned_id[i]
        for uid in user_id:
            if check(bid, uid):
                copy_arr = arr.copy()
                copy_arr.append(uid)
                copy_user_id = user_id.copy()
                copy_user_id.remove(uid)                
                combination(copy_arr, i + 1, copy_user_id, banned_id, max_depth)
                
def check(pattern, ide):
    valid = True
    
    # print(f'패턴 길이 : {len(pattern)}, 아이디 길이 : {len(ide)}')
    if len(pattern) != len(ide):
        valid = False
        return valid
    
    for i in range(len(pattern)):
        if pattern[i] != '*' and pattern[i] != ide[i]:
            valid = False
            break
            
    return valid
            
    
                    
        
    