# Boyer-Moore법으로 문자열을 검색
def bmMatch(txt,pat):
    pt = 0
    pp = 0
    txtLen = len(txt)
    patLen = len(pat)

    # 건너뛰기 표 만들기
    skip = [patLen]*26 # Character.MAX_VALUE 몰라서 일단 알파벳 갯수 26 적음
    for pt in range(patLen-1):
        skip[pat[pt]] = patLen - pt - 1 # pt == patLen-1

    # 검색
    while pt < txtLen:
        pp = patLen - 1

        while txt[pt] == pat[pp]:
            if pp == 0: return pt
            pp -= 1
            pt -= 1
        
        if skip[txt[pt]] > patLen - pp:
            pt += skip[txt[pt]]
        else:
            pt += patLen - pp

    return -1

txt = 'ABCXDEZCABACABAC'
pat = 'ABAC'
print(bmMatch(txt,pat))


    