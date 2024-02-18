for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    ans = 0
    while(i < n):
        if s[i] == '@':
            ans += 1
        elif s[i] == '*':
            i += 1
            if i < n and s[i] == '*':
                break
            elif i < n and s[i] == '@':
                ans += 1
        i += 1
    print(ans)