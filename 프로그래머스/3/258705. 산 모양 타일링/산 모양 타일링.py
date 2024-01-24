def solution(n, tops):
    answer = 0
    div = 10007
    a = [0] * (n + 2)
    b = [0] * (n + 2)
    
    a[0] = 1
    
    for i in range(0, n):
        a[i + 1] = a[i] * (2 + tops[i]) + b[i] * (1 + tops[i])
        b[i + 1] = a[i] + b[i]
        
        a[i + 1] = a[i + 1] % div;
        b[i + 1] = b[i + 1] % div;
    
    return (a[n] + b[n]) % div