# My Code
def solution(arrangement):
    answer = 0
    floor = 0
    flag = 0
    for ele in arrangement:
        if ele == '(': floor += 1; flag = 1
        else:
            if flag == 1: floor -= 1; answer += floor; flag = 0
            else: floor -= 1; answer += 1
    return answer

# Best Code
def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer

print(solution("()(((()())(())()))(())"))