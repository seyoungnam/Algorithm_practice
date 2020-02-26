# KMP법에 의한 문자열 검색
def kmpMatch(txt,pat):
    pt = 1
    pp = 0
    skip = [0]*(len(pat)+1)

    # 건너뛰기 표 생성
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 검색
    pt = pp = 0
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


        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    # pp == len(pat) 이면 pt - pp return 하면서 종료
    if pp == len(pat): return pt - pp + 1
    else: return -1

txt = 'ZABDABCABDADEF'
pat = 'ABCABD'
print("텍스트 : {}".format(txt))
print("패턴   : {}".format(pat))
print(kmpMatch(txt,pat),"번째 문자와 일치합니다.")

