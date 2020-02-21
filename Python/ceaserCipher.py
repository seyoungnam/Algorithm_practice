# 나의 코드
# 1. [ s[i:i+1] for i in range(len(s))] 활용하여 list 생성
# 2. 위 list의 요소를 하나씩 읽음, 공백 아니라면 ord('a')활용하여 n씩 밀고
#    공백이라면 패스

def solution(s, n):
    answer = []
    words = [s[i:i+1] for i in range(len(s))]
    for i in range(len(words)):
        v = ord(words[i])
        if v>=65 and v<=90 : answer.append(chr(v+n) if v+n<=90 else chr(v+n-90+64))
        elif v>=97 and v<=122 : answer.append(chr(v+n) if v+n<=122 else chr(v+n-122+96))
        elif v==32 : answer.append(" ")
    return "".join(answer)

# best code
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

if __name__ == '__main__':
    s1 = "AB"; n1 = 1
    s2 = "z" ; n2 = 1
    s3 = "a B z" ; n3 = 4

    # print("ex1 : ", solution(s1, n1))
    # print("ex2 : ", solution(s2, n2))
    print("ex3 : ", solution(s3, n3))
    print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))

    # print('a : ', ord('a'))
    # print('z : ', ord('z'))
    # print('A : ', ord('A'))
    # print('Z : ', ord('Z'))
    # print("공백 : ", ord(' '))

