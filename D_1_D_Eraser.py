for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = 0
    i = 0
    while i != n and i < n:
        if s[i] == 'B':
            ans += 1
            i += k
        else:
            i += 1
    print(ans)