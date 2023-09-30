a = input()
b = input()
n = len(a)
ans = ''
for i in range(n):
    ans += str(int(a[i]) ^ int(b[i]))
print(ans)