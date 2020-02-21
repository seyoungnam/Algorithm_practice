# My Code
def solution(n, arr1, arr2):
    decimal  = [ (a | b) for a,b in zip(arr1, arr2)]
    binary = [bin(c)[2:] for c in decimal]
    add_binary = []
    for ele in binary:
        add_binary.append('0'*(n - len(ele)) + ele)
    return [''.join(['#' if c == '1' else ' ' for c in ele]) for ele in add_binary]

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))


# Best Code 1
def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# Best Code 2
import re

def solution3(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer