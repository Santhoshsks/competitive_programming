import sys,itertools,functools,collections,math
input = sys.stdin.readline
def solve(ls,n):
    a=[]
    a.append(ls[0])
    for i in range(1,n):
        if ls[i]>=ls[i-1]:
            a.append(ls[i])
        else:
            a.append(ls[i])
            a.append(ls[i])
    print(len(a))
    for i in a:
        print(i,end=' ')
 
for _ in range(int(input())):
    n=int(input())
    ls=[*map(int,input().split())]
 
    solve(ls,n)
    print('')