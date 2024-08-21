for _ in range(int(input())):
    a = list(map(int, input().split()))
    k = a[0]
    n = a[1]
    ans = [1]
    add = 1
    k -= 1
    while n - (ans[-1] + add) >= k - 1 and k > 0:
        ans.append(ans[-1] + add)
        add += 1
        k -= 1
    for i in range(k):
        ans.append(ans[-1] + 1)
    print(*ans, sep = " ")