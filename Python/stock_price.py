# My Code
def solution(prices):
    length = len(prices)
    answer = [0]*length
    for i in range(length-1):
        cnt = length-i-1
        for j in range(i+1,length):
            if prices[i] > prices[j]: cnt = j - i; break
        answer[i] = cnt
    return answer

print(solution([1, 2, 3, 2, 3]))