answer = 1_000_000_000

def solution(begin, target, words):
    global answer
    
    charset = set(char for word in words for char in word)
    visited = [0 for _ in words]
    count = 0
    dfs(begin, charset, count, visited, target, words)
    
    if answer == 1000000000:
        answer = 0
    return answer

def dfs(word, charset, count, visited, target, words):
    if word == target:
        print(word)
        print(count)
        global answer
        answer = min(answer, count)
        return
    
    for c in charset:
        for i in range(0, len(word)):
            l = list(word)
            l[i] = c
            conv = ''.join(l)
            
            if conv in words and visited[words.index(conv)] == 0:
                visited[words.index(conv)] = 1
                dfs(conv, charset, count + 1, visited, target, words)
                visited[words.index(conv)] = 0
            
    
    