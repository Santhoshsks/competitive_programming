n , q = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(q):
    maxi, mini = map(int, input().split())
    l1 = l[:maxi]
    for i in range(maxi, len(l)):
        me = min(l1)
        mi = l1.index(me)
        if l[i] > me:
            l1[mi] = l[i]
    l1.sort()
    l1 = l1[:mini]
    print(sum(l1))