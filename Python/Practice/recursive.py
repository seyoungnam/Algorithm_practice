# 최대공약수(Greatest Common Divisor)
def gcd(x,y):
    if y == 0: return x
    else: return gcd(y,x%y)

x = 22
y = 8
# print("{}와 {}의 최대공약수는 {}".format(x, y, gcd(x,y)))

# 재귀 알고리즘
def recur(n):
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

# 꼬리 재귀의 제거
def recur1(n):
    while n > 0:
        recur1(n-1)
        print(n)
        n = n - 2

# 재귀의 제거
def recur2(n):
    s = []
    while True:
        if n > 0:
            s.append(n)
            n = n - 1
            continue
        if len(s) != 0:
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break

n = int(input())
print(recur2(n))




