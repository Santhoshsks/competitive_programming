n = int(input())
l = list(map(int,input().split()))
mini = 101
maxi = 0
for i in range(n):
    if l[i] <= mini:
        mii = i
        mini = l[i]
    if l[n - i - 1] >= maxi:
        mai = n - i - 1
        maxi = l[n - i - 1]
if mai < mii:
    print((n - mii - 1) + mai)
else:
    print((n - mii - 1) + mai - 1)