def arrVal(x, y):
    return max(x, y) + 1

def solution(n, left, right):
#     y = left // n + 1
#     x = left % n + 1
    
#     end_y = right // n + 1
#     end_x = right % n + 1
    # print(f'y = {y} | x = {x} | end_y = {end_y} | end_x = {end_x}')
    
    answer = []
    
    # gap = end_y - y
    
    for i in range(left, right + 1):
        y = i // n
        x = (i % n)        
        answer.append(arrVal(x, y))
        
    return answer