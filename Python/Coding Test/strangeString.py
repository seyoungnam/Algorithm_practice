# 나의 코드
def solution(s):
    answer =[]
    for word in s.split(' '):
        cha = list(word)
        for i in range(len(word)):
            if i%2 == 0:
                cha[i] = cha[i].upper()
            else:
                cha[i] = cha[i].lower()
        word = "".join(cha)
        answer.append(word)
    return " ".join(answer)

print(solution("tryi hellop worldj"))

# Best Code
def toWeirdCase(s):
    # 함수를 완성하세요
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")))

# Best Code 2
def toWeirdCase2(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

def test(s):
    return [c.upper() if i%2 == 0 else c.lower() for i, c in enumerate(s)]
print(test('tried'))