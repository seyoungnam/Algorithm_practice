# My Code

import re

# def solution(dartResult):
#     # 변수 설정
#     answer = 0
#     pre_answer = 0

#     while len(dartResult) > 0:
#         # 점수 구하기
#         score = re.compile('[0-9]+').match(dartResult).group()

#         # 승수 구하기
#         length = len(score)
#         area = dartResult[length:length+1]
#         multiplier = 0
#         if area == 'S': multiplier = 1
#         elif area == 'D': multiplier = 2
#         else: multiplier = 3

#         # cur_answer에서 (점수^승수) 넣기
#         cur_answer = int(score)**multiplier

#         print("pre_answer=", pre_answer)
#         print("cur_answer=", cur_answer)

#         # cur_answer에 옵션 적용, dart 내 계산 끝낸 unit 지우기
#         option = dartResult[length+1:length+2]
#         if option == '*': answer += pre_answer + cur_answer*2; pre_answer = cur_answer*2; dartResult = dartResult[length+2:]
#         elif option == '#': answer += cur_answer*(-1); pre_answer = cur_answer*(-1); dartResult = dartResult[length+2:]
#         else: answer += cur_answer; pre_answer = cur_answer; dartResult = dartResult[length+1:]
#         print("answer=", answer)

#     return answer

# Best Code
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
            print(dart)
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

print("예제 1: 37?", solution('1S2D*3T'))
print("예제 2: 9?", solution('1D2S#10S'))
print("예제 3: 3?", solution('1D2S0T'))
print("예제 4: 23?", solution('1S*2T*3S'))
print("예제 5: 5?", solution('1D#2S*3S'))
print("예제 6: -4?", solution('1T2D3D#'))
print("예제 7: 59?", solution('1D2S3T*'))


