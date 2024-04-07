def solution(phone_book):
    answer = True
    dt = {}
    phone_book.sort(key = len)
    len_list = []
    len_list.append(int(len(phone_book[0])))
    
    for i, val in enumerate(phone_book):
        if len(val) == len_list[0]:
            dt[val] = dt.get(val, 0) + 1
            continue
        
        for l in len_list:
            key = val[0:l]    
            if dt.get(key, 0) + 1 > 1:
                return False
        dt[val] = 1
        
        if len_list[-1] != len(val):
            len_list.append(len(val))
    return answer