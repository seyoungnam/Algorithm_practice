# My Code
# 1. 한쌍의 숫자를 비교해서 큰 숫자는 앞으로 작은 숫자는 뒤로 배치
# 2. 1번 loop을 돌리고 나면 가장 작은 수가 가장 뒤에 배치
# 3. len을 하나씩 줄이면서 loop을 돌리면 됨
def solution(n):
    num = list(str(n))
    for i in range(len(num)):
        print(i)
        for j in range(len(num)-i-1):
            if num[j] < num[j+1]:
                tem = num[j]
                num[j] = num[j+1]
                num[j+1] = tem
    return int("".join(num))


print(solution(118372))


# Best Code 1
def solution1(n):
    ls = list(str(n))
    ls.sort(reverse = True) # descendingOrder로 재배열해주는 함수
    return int("".join(ls))