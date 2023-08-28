n, target = map(int, input().strip().split())
arr = list(map(int, input().split()))

i = 0
ans = 0

while i < n:
    if arr[i] > 0 and arr[i] >= arr[target-1]:
        ans += 1
    i += 1

print(ans)
