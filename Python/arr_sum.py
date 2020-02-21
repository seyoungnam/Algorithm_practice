# My Code
import numpy as np
def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append(list(np.array(arr1[i])+np.array(arr2[i])))
    return result
        
        

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
ar1 = [1,2]
ar2 = [3,4]
print("결과 : {}".format(solution(arr1, arr2)))

# Best Code
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer