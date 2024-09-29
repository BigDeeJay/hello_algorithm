def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 초기 각도를 계산하고 1초씩 늘려서 생기는 각도의 변화에 따라 겹치는지 여부 확인
    start = time_to_seconds(h1, m1, s1)
    end = time_to_seconds(h2, m2, s2)
    
    prev_angles = []
    
    for seconds in range(start, end + 1):
        # print('seconds', seconds)
        h, m, s = seconds_to_time(seconds)
        current_angles = calculate_clock_hand_angle(seconds)
        hour_angle, minute_angle, second_angle = current_angles
        
        # 초기에 일치하는지 확인
        if second_angle == hour_angle or second_angle == minute_angle:
            prev_angles = current_angles
            answer += 1
            continue
            
        # 다음 순회 전 현재 세컨드 앵글 저장
        if len(prev_angles) == 0:
            prev_angles = current_angles
            continue
        else:
            prev_hour_angle, prev_minute_angle, prev_second_angle = prev_angles
            
            # print(f'prev_angles = {prev_angles}, current_angles = {current_angles}')
            
            if prev_second_angle == 354:
                second_angle = 360
                        
            if (prev_second_angle < prev_hour_angle and second_angle >= hour_angle):
                answer += 1
            if (prev_second_angle < prev_minute_angle and second_angle >= minute_angle):
                answer += 1
                
            prev_angles = current_angles
            
    return answer

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return [h, m, s]

def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def calculate_clock_hand_angle(seconds):
    h, m, s = seconds_to_time(seconds)
    
    hour_angle = (h % 12 * 30) + (m * 30 / 60) + (s * 30 / 3600)
    minute_angle = (m * 6) + (s * 6 / 60)
    second_angle = s * 6
    
    return [hour_angle, minute_angle, second_angle]
    