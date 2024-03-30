def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key = lambda x : x * 4, reverse = True)
    return str(int(''.join(nums)))