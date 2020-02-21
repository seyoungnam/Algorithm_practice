# 나의 코드 : 마지막 테스트에서 막힘
# lambda, reduce 쓰면 될 것 같음.
from functools import reduce
def solution(n):
    return reduce(lambda x,y: int(x)+int(y), list(str(n)))

print(solution(123))
print(solution(987))

# 나의 코드 2 : 통과 코드
from functools import reduce
def solution2(n):
    answer = 0
    for num in list(str(n)):
        answer += int(num)
    return answer

# Best Code : 재귀함수 활용
def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))

# Best Code2
def sum_digit2(number):
    return sum([int(i) for i in str(number)])
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))