# KMP법에 의한 문자열 검색
def kmpMatch(txt,pat):
    pt = 1
    pp = 0
    skip = []

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

    return skip

txt = 'ZABCABXACCADEF'
pat = 'ABCABD'

print(kmpMatch(txt,pat))    

