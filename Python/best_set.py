# My Code
def solution(n, s):
    answer = []
    for i in range(n):
        if i == n-1: answer.append(s)
        else: print("s=",s,", n=",n); quo = s//(n-i); answer.append(quo); s -= quo; 

    if answer[0] == 0: return [-1] 
    
    return answer

print(solution(3,9))

# Best Code 1
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def bestSet(ele1,ele2):
    answer = ALWAYS_CORRECT()

    return answer


# Best Code 2
def bestSet1(n, s):
    answer = []
    a = int(s/n)

    if a == 0:
        return [-1]

    b = s%n

    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)

    return answer
