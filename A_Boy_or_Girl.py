from collections import defaultdict
s = input()
st = set()

for i in s:
    st.add(i)

if len(st) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")