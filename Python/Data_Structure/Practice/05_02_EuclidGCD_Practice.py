# 재귀 메서드 호출을 사용하지 않고 실습5-2의 gcd 메서드를 작성하세요.
def gcd(x,y):
    while y != 0:
        temp = y
        y = x%y
        x = temp
    return x

print(gcd(22,8))