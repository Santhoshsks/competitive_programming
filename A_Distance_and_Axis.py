for _ in range(int(input())):
    n, k = map(int, input().split())
    if n<k:
        print(abs(k-n))
    else:
        if (n-k) % 2 == 0:
            print(0)
        else:
            print(1)