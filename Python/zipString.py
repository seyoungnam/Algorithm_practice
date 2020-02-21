#나의 풀이
def solution1(s):
    minLength = len(s)
    for i in range(1,len(s)):
        curLength = len(s)
        unit = 'T'
        for j in range(0, len(s), i):
            if unit == s[j+i:j+2*i]:
                curLength -= i
            elif s[j:j+i] == s[j+i:j+2*i]:
                curLength -= i-1
                unit = s[j:j+i]    
        if curLength < minLength:
            minLength = curLength
    return minLength

#나의 풀이2
def solution2(s):
    minLen = len(s)
    for i in range(1, len(s)):
        curLen = len(s)
        count = 0
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+2*i]:
                curLen -= i
                count += 1
            else: count = 0
            if count == 1:
                curLen += 1
        if curLen < minLen:
            minLen = curLen
    return minLen

# 다른 사람 풀이
def solution3(s):
   l = len(s); ans=l
   for i in range(1, (l//2)+1):
       prev=s[:i];j=i;flag=1;tl=l
       while 1:
           if j+i > l: break
           if prev == s[j:j+i]:
               flag+=1; tl-=i
           else:
               if flag>1: tl+=len(str(flag))
               flag=1
               prev=s[j:j+i]
           j+=i
       if flag>1: tl+=len(str(flag))
       ans = min(ans, tl)
   return ans

# 베스트 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, len(text)//2 + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))

# if __name__ == '__main__':
#     a = "aabbaccc"
#     b = "ababcdcdababcdcd"
#     c = "abcabcdede"
#     d = "abcabcabcabcdededededede"
#     e = "xababcdcdababcdcd"

#     print(solution2(a))
#     print(solution2(b))
#     print(solution2(c))
#     print(solution2(d))
#     print(solution2(e))