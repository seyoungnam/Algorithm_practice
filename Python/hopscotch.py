# My Code
# def solution(land):
#     answer = []
#     for i in range(len(land[0])):
#         candidate = land[0][i]
#         taken = i
#         for j in range(1,len(land)):
#             row_dict = {}
#             for k,val in enumerate(land[j]):
#                 if k != taken: row_dict[k] = val
#             max_val = max(row_dict.values())
#             candidate += max_val
#             for ele in row_dict.items():
#                 if ele[1] == max_val: taken = ele[0]
#         answer.append(candidate)
#     return max(answer)

# Reference Code
def solution2(land):
    for i in range(len(land)-1):
        land[i+1][0] = max(land[i][1], land[i][2], land[i][3]) + land[i+1][0]
        land[i+1][1] = max(land[i][0], land[i][2], land[i][3]) + land[i+1][1]
        land[i+1][2] = max(land[i][0], land[i][1], land[i][3]) + land[i+1][2]
        land[i+1][3] = max(land[i][0], land[i][1], land[i][2]) + land[i+1][3]
    
    return max(land[-1])

# Reference Code 2
def solution(land):
    result = 0
    for i in range(1,len(land)):
        for j in range(4):
            temp = land[i-1][:]
            temp[j] = 0
            land[i][j]+=max(temp)
    result = max(land[-1])
    return result

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))


