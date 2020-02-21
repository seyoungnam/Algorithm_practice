# 나의 코드
def solution(n):
    answer=[]
    for i in range(1,n+1):
        if i%2 != 0: answer.extend('수')
        else: answer.extend('박')
    return "".join(answer)

# best code
def solution2(n):
    s = "수박" * n
    return s[:n]

# 다른 코드
def solution3(n):
    return "수박"*(n//2) + "수"*(n%2)
        
if __name__ == '__main__':
    n = 3
    m = 4
    print(solution(n))
    print(solution(4))