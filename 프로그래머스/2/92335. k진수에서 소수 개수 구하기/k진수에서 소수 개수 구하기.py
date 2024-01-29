def solution(n, k):
    answer = 0
    for str in convert_notation(n, k).split("0"):
        if len(str) > 0 and int(str) > 1 and check_prime(int(str)):
            answer += 1
    return answer

def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]

def check_prime(num):
    valid = True
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i == 0):
            valid = False
    return valid