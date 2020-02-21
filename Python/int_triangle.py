# My Code
def solution(triangle):
    for i in range(1,len(triangle)):
        print("i={}".format(i))
        last_loc = len(triangle[i])-1
        triangle[i][0] = triangle[i-1][0] + triangle[i][0]
        for j in range(1, last_loc):
            triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
        triangle[i][last_loc] = triangle[i-1][last_loc-1] + triangle[i][last_loc]
             
    return max(triangle[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print("최종답: {}".format(solution(triangle)))