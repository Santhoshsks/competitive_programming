def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(1, n + 1):
        if a[i] < a[i - 1] + a[i + 1]:
            print("NO")
            return
        a[i] -= min(a[i - 1], a[i + 1])
        a[i + 1] -= min(a[i - 1], a[i + 1])
        a[i - 1] = 0
    print("YES" if a[n] == 0 else "NO")

t = int(input())
for _ in range(t):
    solve()
