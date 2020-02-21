# 나의 코드
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            val = i
    return '김서방은 %d에 있다' % (val)

# 다른 사람 코드
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

if __name__ == '__main__':
    seoul = ["Jane", "Kim", "Sup"]
    print(solution(seoul))
