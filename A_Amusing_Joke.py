from collections import defaultdict
a = input()
b = input()
c = input()
d = defaultdict(int)

for i in a:
    d[i] += 1
for i in b:
    d[i] += 1
for i in c:
    d[i] -= 1
    
flag = False
for i in d.values():
    if i != 0:
       flag = True

if flag:
    print("NO")
else:
    print("YES")