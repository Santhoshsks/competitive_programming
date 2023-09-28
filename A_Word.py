s = input()
n = len(s)
low = 0
up = 0
for i in range(n):
    if s[i].lower() == s[i]:
        low += 1
    else:
        up += 1

if low == up:
    print(s.lower())
elif low < up:
    print(s.upper())
else:
    print(s.lower())