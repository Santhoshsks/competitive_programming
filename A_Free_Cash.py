from collections import defaultdict

d = defaultdict(int)

for _ in range(int(input())):
    a, b = map(str, input().split())
    if len(a) == 1:
        a = '0' + a
    if len(b) == 1:
        b = '0' + b
    d[a+b] += 1

print(max(d.values()))