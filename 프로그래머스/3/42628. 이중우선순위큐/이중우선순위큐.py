import heapq

def solution(operations):
    min_heap, max_heap = [], []
    for oper in operations:
        o = oper.split(" ")
        if o[0] == "I":
            heapq.heappush(min_heap, int(o[1]))
            heapq.heappush(max_heap, -int(o[1]))
        elif o[0] == "D":
            if not min_heap and not max_heap:
                continue
            if o[1] == "-1":
                max_heap.remove(-heapq.heappop(min_heap))
            elif o[1] == "1":
                min_heap.remove(-heapq.heappop(max_heap))
                
    answer = []
    
    if min_heap and max_heap:
        answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        answer = [0, 0]
        
    return answer