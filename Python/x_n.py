# My Code
def solution(x, n):
    if x>0: return [i for i in range(x,x*n+1,x)] 
    elif x<0: return [i for i in range(x,x*n-1,x)]
    else: return [0 for i in range(x,x+n)]
    
print("정답 : {}".format(solution(0,2)))

# Best Code
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))