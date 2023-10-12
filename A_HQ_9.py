input = input()
flag = True
for i in input:
    if i in ['H','Q','9']:
        flag = False
    
if flag:
    print("NO")
else:
    print("YES")