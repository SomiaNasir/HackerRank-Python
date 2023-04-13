# https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())
a = 1

for i in range(0, N//2):
    print(('.|.' * a).center(M, '-'))
    a = a + 2
    
print('WELCOME'.center(M, '-'))

for i in range(0, N//2):
    a = a - 2
    print(('.|.' * a).center(M, '-'))
    
