# My Code
# stages.sort() 후 N 순서대로 카운팅한 개수를 분자, 전체 길이를 분모로 넣고 실패율 계산, "1: 실패율" 의 형태로 dict에 넣는다 
# 다음번 분모 계산 시에는 전체 길이에서 이전 분자를 빼준다.
# dict 내 key를 실패율 높은 순서대로 result list에 append

def solution(N, stages):
    numerator = 0
    denominator = len(stages)
    result_dict = {}
    result_list = []
    
    for i in range(1,N+1):
        denominator -= numerator
        numerator = stages.count(i)
        if numerator != 0: result_dict[i] = numerator/denominator
        else: result_dict[i] = 0
        
    
    sdict = sorted(result_dict.items(), reverse=True, key=lambda x: x[1]) # sort by value in descending order
    # print(sdict)
    for ele in sdict:
        result_list.append(ele[0])
    return result_list



# 참고
# slist = sorted(result_dict.items()) # sort by key in ascending order
# slist = sorted(result_dict.items(), reverse=True) # sort by key in descending order
# slist = sorted(result_dict.items(), key=lambda x:x[1]) # sort by value in ascending order
# slist = sorted(result_dict.items(), key=lambda x:x[1]) # sort by value in descending order

# Best code
def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    print(result)
    return sorted(result, key=lambda x : result[x], reverse=True)

print(solution2(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution2(4, [4,4,4,4,4]))