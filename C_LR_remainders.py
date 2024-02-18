for _ in range(int(input())):
    n, m = map(int, input().split())
    lis = list(map(int, input().split()))
    cmd = input()
    ans = []
    for p in cmd:
        temp = 1
        for i in lis:
            temp *= i
        ans.append(str(temp % m))
        if p == 'L':
            lis.pop(0)
        else:
            lis.pop(-1)
    print(' '.join(ans))

