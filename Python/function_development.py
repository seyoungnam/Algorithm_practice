# My Code
def solution1(progresses, speeds):
    answer = []
    days = []
    for x,y in zip(progresses, speeds):
        quo, rem = divmod(100-x, y)
        if rem != 0: days.append(quo + 1)
        else: days.append(quo)
    
    comp = -1
    for i in range(len(days)):
        if comp >= days[i]:
            answer[-1] += 1
        else:
            answer.append(1)
            comp = days[i]               
    return answer

# Best Code
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

print(solution([93,30,55], [1,30,5]))