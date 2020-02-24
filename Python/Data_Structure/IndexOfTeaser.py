def indexOfTester(txt,pat):
    try:
        idx1 = txt.index(pat)
        idx2 = txt.rindex(pat)
    except ValueError:
        return "텍스트 안에 패턴이 없습니다."
    len1 = 0
    len2 = 0
    for i in range(idx1):
        len1 += len(txt[i].encode())
    for i in range(idx2):
        len2 += len(txt[i].encode())
    print(len1,len2)
    
    line1 = "텍스트 :"+txt
    line2 = "패턴   :%{}s".format(len1)%pat
    line3 = "텍스트 :"+txt
    line4 = "패턴   :%{}s".format(len2)%pat

    return line1+'\n'+line2+'\n'+line3+'\n'+line4

txt = 'AB주이지스DEF이지스12'
pat = '이지스'

print(indexOfTester(txt,pat))
    