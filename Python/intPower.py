# My Code
# 1. sqrt(x) 결과가 int이면, pow(x+1)을 리턴하고 아니라면 -1 리턴
import math
def solution(n):
    num = math.sqrt(n)
    return math.pow(num+1,2) if math.ceil(num) - num == 0 else -1

print(solution(121))

# Best Code 1
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0: # 중요
        return (sqrt + 1) ** 2
    return 'no'

