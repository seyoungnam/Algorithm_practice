# [문제접근 방식]
# 0. return 조건: pat의 마지막까지 txt의 문자와 같을 경우(즉, pp == len(pat)) 혹은 txt를 끝까지 읽는동안 pat과 같은 문자를 찾지 못했을 경우(pt == len(txt))
# 1. txt와 pat의 문자를 뒤에서 하나씩 읽는다.
# 2. 만약 문자가 같다면 앞문자를 읽는다.
#    문자가 다르다면 txt의 시작점을 -1 옮긴 후 문자와 pat의 끝문자부터 다시 비교한다.

def bfMatchRev(txt, pat):
    pt = len(txt)-1
    pp = len(pat)-1

    while pt != -1 and pp != -1:
        print("pt={}, txt[pt]={}".format(pt,txt[pt]))
        print("pp={}, pat[pp]={}".format(pp,pat[pp]))
        if txt[pt] == pat[pp]:
            pt -= 1
            pp -= 1
        else:
            pt = pt - pp + len(pat) -2
            pp = len(pat)-1
        

    if pp == -1: return pt + 2 
    else: return -1

txt = 'ABABCDEFGHA'
pat = 'ABC'

print("패턴 위치는 {}번째 입니다.".format(bfMatchRev(txt,pat)))