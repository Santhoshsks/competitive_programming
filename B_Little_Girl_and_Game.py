s = input().strip()

count = 0
se = set()
for i in s:
    if i not in se:
        if s.count(i) % 2:
            count += 1
        se.add(i)

if count == 1:
    print("First")
elif count % 2:
    print("First")
else:
    print("Second")