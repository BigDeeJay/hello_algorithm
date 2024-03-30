import heapq

def solution(jobs):
    length = len(jobs)
    maxTime = 100_000_000
    heap = []
    
    total = 0
    
    # jobs.sort(key = lambda x : (x[0], x[1]))

    tasks = []
    taskEndTime = 0

    for t in range(0, maxTime):
        for index, job in reversed(list(enumerate(jobs))):
            if t == job[0]:
                tasks.append(jobs.pop(index))
                # print(tasks)

        optIndex = -1
        optTime = 1001
                
        for i, task in enumerate(tasks):
            if optTime > task[1]:
                optTime = task[1]
                optIndex = i
                
        if t >= taskEndTime and len(tasks) > 0:
            taskEndTime = t + tasks[optIndex][1]
            workTime = taskEndTime - tasks[optIndex][0]
            total += workTime
            # print("t = " + str(t) + ", taskEndTime = " + str(taskEndTime) + ", task = " + str(tasks[optIndex][0]) + ", workTime = " + str(workTime))
            del tasks[optIndex]
        
        if len(jobs) == 0 and len(tasks) == 0:
            break
        
    return total // length