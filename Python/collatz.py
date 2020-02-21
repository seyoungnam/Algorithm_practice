# My Code
def solution(n):
    i = 0
    while n != 1:
        if n%2 == 0: n //= 2 
        else: n = (n*3) + 1
        i += 1
        if i == 500: return -1
    return i

print("n=6, result=", solution(6))
print("n=16, result=", solution(16))
print("n=626331, result=", solution(626331))

    
# Best Code
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))