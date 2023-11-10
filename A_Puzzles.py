n, m = map(int, input().split()) 
f = list(map(int, input().split()))
 
f.sort()
min_diff = f[n-1] - f[0]
 
for i in range(1, m-n+1):
  diff = f[i+n-1] - f[i] 
  if diff < min_diff:
    min_diff = diff
 
print(min_diff)