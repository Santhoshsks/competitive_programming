n , q = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(q):
    maxi, mini = map(int, input().split())
    l1 = l[:maxi]
    for i in range(maxi, len(l)):
        m = l[i]
        for j in range(maxi):
            if m > l1[j]:
                temp = l1[j]
                l1[j] = m
                m = temp
        
    l1.sort()
    l1 = l1[:mini]
    print(sum(l1))