def solution(n, tops):
    answer = 0
    div = 10007
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    
    a[0] = 1
    
    for i in range(0, n):
        if (tops[i] == 1):
            a[i + 1] = a[i] * 3 + b[i] * 2
        else: 
            a[i + 1] = a[i] * 2 + b[i] * 1
        b[i + 1] = a[i] + b[i]
        
        a[i + 1] = a[i + 1] % div;
        b[i + 1] = b[i + 1] % div;
    
    return (a[n] + b[n]) % div