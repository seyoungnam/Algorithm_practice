# My Code
# def solution(N):
#     answer = 4
#     length_list = [0,1]
#     for i in range(2,N+1):
#         # print(length_list[-2:])
#         length_list.append(sum(length_list[-2:]))
#         answer += length_list[i]*2
#     return answer

# Reference Code
def solution(N):
    dp = [0] * int(N+2)
    if N == 1: return 4
    if N == 2: return 6
    dp[0], dp[1], dp[2] = 0, 1, 1
    for i in range(3, N+2):
        dp[i] = dp[i-1] + dp[i-2]
    return 2*dp[N-1] + 4*dp[N]

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))

# 0(0, 0)
# 1(1, 1*4) 
# 2(0+1 = 1, 1*4 - 1*2 = 6)
# 3(1+1 = 2, 6 +2*2 = 10)
# 4(2+3 = 5, 10 +5*2 = )