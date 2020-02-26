def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1


print("정수를 입력하세요 : ")
n = int(input())
print(n,"의 팩토리얼은 ",factorial(n),"입니다.")

