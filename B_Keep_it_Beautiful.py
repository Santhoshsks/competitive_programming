for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    i = 0
    ans = ""
    mini = l[0]
    maxi = l[0]
    while i < n:
        if l[i] >= maxi:
            maxi = l[i]
            ans += "1"
            i += 1
        elif l[i] <= mini:
            ans += "1"
            maxi = mini
            mini = l[i]
            i += 1
            break
        else:
            ans += "0"
            i += 1
    while i < n:
        if l[i] >= mini and l[i] <= maxi:
            ans += "1"
            mini = l[i]
            i += 1
        else:
            ans += "0"
            i += 1
    print(ans)