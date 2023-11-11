s = input()

t = "olleh"

for i in s:
    if t:
        if t[len(t) - 1] == i:
            t = t[:-1]
if t == "":
    print("YES")
else:
    print("NO")