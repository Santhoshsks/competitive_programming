n = int(input())
s = input()
l = ''
flag = -1
ans = ''

if len(s) == 1:
    print(s)

else:

    for i in s:
        if flag == -1:
            ans += i
            flag = 0
        elif flag == 0:
            ans = i + ans
            flag = 1
        else:
            ans += i
            flag = 0
    if len(s) % 2 == 0:
        print(ans[::-1])
    else:
        print(ans)