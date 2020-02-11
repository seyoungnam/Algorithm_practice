# My Code


# def solution(skill, skill_trees):
#     answer = 0
#     skill_dict = {}
#     skill_list = list(skill)
#     for i,c in enumerate(skill_list):
#         skill_dict[c] = i

#     num_list = []
#     for ele in skill_trees:
#         num_ele_list = []
#         ele_list = list(ele)
#         for c in ele_list:
#             for key in skill_dict.keys():
#                 if c == key: num_ele_list.append(skill_dict[key])
#         num_list.append(num_ele_list)
#     print(num_list)

#     for ele in num_list:
#         length = len(ele)
#         if length == 0: answer += 1
#         elif length == 1 and ele == [0]: answer += 1
#         elif length == 2 and ele == [0,1]: answer += 1
#         elif length == 3 and ele == [0,1,2]: answer += 1

#     return answer

# Best Case 1
def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        a = [tree.index(i) for i in skill if i in tree]
        a_ = sorted(a)
        if a == a_ and all(i in tree for i in skill[:len(a)]): cnt += 1
    return cnt

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# Best Case 2
def solution2(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
