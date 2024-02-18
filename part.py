from collections import Counter
k=int(input())
l=eval(input())
if len(l)%k!=0:
    print("No")
else:
    x=len(l)/k
    q=Counter(l)
    flag=True
    for i in q.values():
        if i>k:
            flag=False
            break
    if flag==True:
        print("Yes")
