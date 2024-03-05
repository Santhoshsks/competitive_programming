for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    l.sort()
    l1 = []
    maxi = l[-1]

    def mex(l2):
        ans = 0
        for i in l2:
            if i == ans:
                ans += 1
        return ans
    
    for i in l:
        if i == mex:
            mex += 1
        if l1 == []:
            l1.append([i])
        else:
            f = True
            for j in l1:
                if i in j:
                    pass
                else:
                    f = False
                    j.append(i)
                    break
            if f:
                l1.append([i])
    m = mex(l1[0])
    
    f =True
    for i in l1:
        if mex(i) != m:
            f = False
    m = len(l1)
    if f and m > 1:
        print(m)
        if m * 2 > maxi:
            for i in range(1,m + 1):
                print(i,i)
        else:
            a = 1
            ad = maxi // m
            
            for i in range(1,m + 1):
                print(a, a + ad)
                a += ad + 1
    else:
        print(-1)
