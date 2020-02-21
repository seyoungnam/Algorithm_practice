# My Code
def solution(numbers):
    answer = 0
    can_set = set([])
    for _ in range(len(numbers)):
        for i in range(1,len(numbers)+1):
            if int(numbers[0:0+i]) != 0: can_set.add(int(numbers[0:0+i]))        
        numbers = numbers[1:] + numbers[0]
    print("can_set={}".format(can_set))
    for val in can_set:
        if isPrime(val) == True: answer += 1      
    return answer

def isPrime(n):
    if n == 1: return False
    elif n%2 == 0: return n == 2
    for i in range(3,n,2):
        if n%i == 0: return False
    return True

print(solution("011"))
print(solution("17"))


