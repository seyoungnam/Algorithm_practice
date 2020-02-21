# 나의 코드
# 1. 나머지가 없는 경우만 골라서 list에 넣고 나중에 sum
import math
def solution(n):
    answer = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        if n%i == 0 : answer += i + n//i
    return answer

def solution2(n):
    answer = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        quo, remainder = divmod(n, i)
        if remainder == 0 : answer += quo + i
    return answer
    
# 다른 사람 풀이
def solution3(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 0:
            answer += i
    return answer

# Best Code
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

print(sumDivisor(5))