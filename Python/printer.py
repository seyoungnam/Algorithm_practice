# My Code
def solution(priorities, location):
    answer = 0
    while len(priorities) != 0:

        if priorities[0] != max(priorities): priorities.append(priorities.pop(0)); location -= 1
        else:
            if location != 0: priorities.pop(0); answer += 1; location -= 1
            else: answer += 1; break
        
        if location == -1: location = len(priorities) - 1

    return answer

# Best Code
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print("answer=", solution([2, 1, 3, 2], 2))
print("answer=", solution([1, 1, 9, 1, 1, 1], 0))