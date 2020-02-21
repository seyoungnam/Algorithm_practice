# My Code
# 1. 숫자 두개씩 차례로 비교하여 둘 중 작은 수의 위치와 값을 저장
# 2. loop이 종료되면 해당 숫자를 없앰

def solution(arr):
    length = len(arr)
    if length > 1:
        smallest = arr[0]
        for i in range(1,length):
            if arr[i] < smallest:
                smallest = arr[i]
        arr.remove(smallest)
    else: return [-1]
    return arr

print(solution([4,3,2,1]))
print(solution([10]))

# Best Code
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]