for _ in range(int(input())):
    s = input()
    ans = 0
    temp = 0
    dig = 1
    for i in s:
        if i == '+':
            dig = 1
            ans = temp
            temp = 0
        else:
            temp = (temp * dig) + int(i)
            dig = dig * 10
    print(temp + ans)
