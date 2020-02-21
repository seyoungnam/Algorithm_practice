# My Code
def solution(arr, budget):
    result = 0
    arr.sort()
    for c in arr:
        if c <= budget:
            budget -= c
            result += 1
    return result

print(solution([1,3,2,5,4],9))

# Best Code
def solution1(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
