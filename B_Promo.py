a=list(map(int,input().split()))
b=list(map(int,input().split()))
b.sort(reverse=True)
req=[b[0]]
for i in range(1,len(b)):
    req.append(req[-1]+b[i])
for i in range(a[1]):
    k=list(map(int,input().split()))
    if k[0]-k[1]==0:
        print(req[k[0]-1])
    else:
        print(req[k[0]-1]-req[k[0]-k[1]-1])