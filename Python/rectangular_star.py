# My Code
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)

# Best Code
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)