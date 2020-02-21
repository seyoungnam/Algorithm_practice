# My Code
def solution(num):
    length = len(num)
    covered = []
    for i,c in enumerate(num):
        if i<length-4: covered.append('*')
        else: covered.append(c)
    return "".join(covered)

num = "027778888"
print("입력값: {}, 출력값: {}".format(num, solution(num)))

# Best Code
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
    