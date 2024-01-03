def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    s_total = getTotalTime(h1, m1, s1) 
    e_total = getTotalTime(h2, m2, s2)
    
    if (s_total == 0 or s_total == 12 * 3600):
        answer += 1
    
    for time in range(s_total, e_total):
        # 현재 위치
        s_sec = time * 6 % 360
        s_min = time * (6 / 60) % 360
        s_hour = time  * (30 / 3600) % 360
        
        # 1초 뒤 위치
        e_sec = (time + 1) * 6 % 360
        e_min = (time + 1) * (6 / 60) % 360
        e_hour = (time + 1)  * (30 / 3600) % 360
        
        e_sec = 360 if e_sec == 0 else e_sec
        e_min = 360 if e_min == 0 else e_min
        e_hour = 360 if e_hour == 0 else e_hour
        
        if (s_sec < s_hour and e_sec >= e_hour):
            answer += 1
        if (s_sec < s_min and e_sec >= e_min):
            answer += 1
        if (e_sec == e_min and e_min == e_hour):
            answer -= 1
    return answer

def getTotalTime(h, m, s):
    return h * 3600 + m * 60 + s