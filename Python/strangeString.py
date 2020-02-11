# 나의 코드
# 1. 공백 기준으로 단어를 분류한다
# 2. 단어를 다시 list화 한 다음 홀수번째는 uppercase 적용
def solution(s):
    answer = []
    for word in s.split():
        word_changed = ""
        for i in range(len(word)):
            if i%2 == 0:
                word_changed = "".join(word[i].upper()) 
            else:
                word_changed = "".join(word[i].lower()) 
        answer.append(word_changed)
    return " ".join(answer)

print(solution("try hello world"))