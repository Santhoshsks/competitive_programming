for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = []
    
    aa = sorted(a)
    b.sort()

    for i in range(n):
        d[aa[i]].append(b[i])
    print(d)
    print('a',a)
    b = []

    for i in a:
        b.append(d[i].pop())
    print('b',b)
    print(' '.join(map(str, b)))