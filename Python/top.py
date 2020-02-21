# My Code
def solution2(heights):
    answer = [0,]
    for i,sender in enumerate(heights[1:]):
        print("i, sender: ", i, sender)
        loc = 0
        receiver_list = heights[:i+1]
        for j in range(len(receiver_list)):
            receiver = receiver_list.pop()
            if receiver > sender: loc = i-j+1; break
        answer.append(loc)
    return answer

# Best Code
def solution(h):
    a = [0]
    for i in range(len(h) - 1, 0, - 1):
        for j in range(i - 1, - 1, - 1):
            if h[i] < h[j]:
                a.insert(1, j + 1)
                break
        else:
            a.insert(1, 0)
    return a

h1 = [6,9,5,7,4]
h2 = [3,9,9,3,5,7,2]
h3 = [1,5,3,6,7,6,5]

print("[0,0,2,2,4]? ",solution(h1))
print("[0,0,0,3,3,3,6]? ",solution(h2))
print("[0,0,2,0,0,5,6]? ",solution(h3))