zero_count = 0
call_count = 0

def solution(s):
    if s == '1':
        return [0, 0]
    
    q = []
    q.append(s)
    while q:
        val = check(q.pop())
        if val != '1':
            q.append(val)
    return [call_count, zero_count]

def check(s):
    global zero_count
    global call_count
    
    call_count += 1
    zero_count += s.count('0')
    new_str = bin(len(s.replace('0', ''))).replace('0b', '')
    # print(f'new_str = {new_str}')
    return new_str