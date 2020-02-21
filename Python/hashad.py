# My Code
def solution(x):
    return True if x % sum([int(n) for n in list(str(x))]) == 0 else False

print("arr={}, return={}".format(10, solution(10)))
print("arr={}, return={}".format(12, solution(12)))

# Reference Code
def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) 

print("test : {}".format(solution(10)))

# Best Code
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0