# [문제접근 방식]
# 0. return 조건: pat의 마지막까지 txt의 문자와 같을 경우(즉, pp == len(pat)) 혹은 txt를 끝까지 읽는동안 pat과 같은 문자를 찾지 못했을 경우(pt == len(txt))
# 1. txt와 pat의 문자를 하나씩 읽는다.
# 2. 만약 문자가 같다면 다음 문자를 읽는다.
#    문자가 다르다면 txt의 시작점을 +1 옮긴 후 문자와 pat의 첫문자부터 다시 비교한다.
def bfMatch(txt, pat):
    pt = 0
    pp = 0
    count = 0
    k = -1

    while pt != len(txt) and pp != len(pat):
        # 패턴 옮긴 횟수 프린트(4칸 띄움)
        if k == pt - pp:
            print("    ", end="")
        else:
            k = pt - pp
            print("%2d  "%k, end="")
            
        # txt 프린트
        for i in range(len(txt)):
            print(txt[i] + " ", end="")
        print("")

        # txt문자와 pat의 문자가 같으면 +, 다르면 | 프린트, +4는 앞부분 4칸 추가하기 위함
        for _ in range(0,pt*2+4):
            print(" ", end= "")
        print('+' if txt[pt] == pat[pp] else '|')

        # pattern 프린트 전 앞공간 남기기
        for _ in range(0,(pt-pp)*2+4):
            print(" ", end="")

        # pattern 프린트
        for i in range(len(pat)):
            print(pat[i] + " ", end="")
        print("")
        print("")
        count += 1


        # pp가 len(pat)되기 전 판별 방식 제시
        # 만약 txt와 pat의 문자가 같다면, 다음 문자 읽기
        # txt와 pat문자가 다르다면 txt시작점을 1 증가시키고 pat은 처음부터 읽기
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    print("비교는 %d회였습니다.\n"%count)
    if pp == len(pat):
        return pt - pp
    return -1

txt = 'ABABCDEFGHA'
pat = 'ABC'

print(bfMatch(txt,pat))
