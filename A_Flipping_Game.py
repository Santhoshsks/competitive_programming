
n = int(input())
l = list(map(int, input().split()))

def invert(l, s, e):
    temp = l.copy()
    for i in range(s, e):
        temp[i] = 1 - temp[i]
    return temp

maxi = sum(l)
if maxi != len(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            ans = sum(invert(l, i, j + 1))
            if maxi < ans:
                maxi = ans
    print(maxi)

else:
    print(maxi - 1)