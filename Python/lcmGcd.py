# My Code

def common_divisor(n):
    answer = [i for i in range(1, n//2+1) if n%i == 0]
    answer.append(n)
    return answer

def gcd(n,m):
    b1 = common_divisor(n)
    b2 = common_divisor(m)
    b3 = list(set(b1).intersection(b2))
    return max(b3)

def lcm(n,m):
    return n*m//gcd(n,m)

def solution(n,m):
    return [gcd(n,m),lcm(n,m)]

print(solution(2,5))
            

# Best Code
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))