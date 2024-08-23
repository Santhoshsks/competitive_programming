for _ in range(int(input())):
    x,y,a,b=map(int,input().split())
    one=[i for i in range(min(x,y)+1,max(x,y))]
    if (a in one and b in one) or (a not in one and b not in one):
        print("NO")
    else:
        print("YES")