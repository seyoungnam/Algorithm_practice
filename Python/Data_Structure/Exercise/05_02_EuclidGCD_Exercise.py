# 유클리드 호제법으로 최대공약수 구하기
def gcd(x,y):
    if y == 0: return x
    else: return gcd(y, x%y)

print("두 정수의 최대공약수를 구합니다.")
print("첫번째 정수를 입력하세요. : "); x = int(input())
print("두번째 정수를 입력하세요. : "); y = int(input())
print("최대공약수는 ",gcd(x,y),"입니다.")