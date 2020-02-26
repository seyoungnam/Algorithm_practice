# 재귀 메서드 호출을 사용하지 않고 실습 5-1의 factorial 메서드를 작성하세요.
def factorial1(n):
    answer = 1
    while n > 0:
        answer *= n
        n -= 1
    return answer

n = 5
print(factorial1(n))