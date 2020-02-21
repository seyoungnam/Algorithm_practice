# 나의 코드
# 자연수 n을 10으로 계속 나눠 나머지만 list로 뽑는다.
def solution(n):
    answer = []
    while n>0:
        quo, rem = divmod(n, 10)
        answer.append(rem)
        n = quo
    return answer

print(solution(12345)) 

# Best Code 1
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

print(digit_reverse(12345))

# Best Code 2
def digit_reverse2(n):
    return [int(i) for i in str(n)][::-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse2(12345)))