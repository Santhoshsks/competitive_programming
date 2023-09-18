for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    zer = 0
    f = False
    for i in l:
        if i == 0:
            zer += 1
        elif i >= 2:
            f = True
        
    if (n + 1) // 2 >= zer:
        print(0)
    elif n == zer or f:
        print(1)
    else:
        print(2)

