n = int(input())
l = list(map(int, input().split()))
mini, maxi = l[0], l[0]

ans = 0

for i in range(1,n):
    if l[i] < mini:
        ans += 1
        mini = l[i]
    elif l[i] > maxi:
        ans += 1
        maxi = l[i]

print(ans)