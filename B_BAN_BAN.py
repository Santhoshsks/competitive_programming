for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        print(1,3)
    else:
        if not (n % 2):
            a = 1
            b = 9
            print(n // 2)
            for i in range(n // 2):
                print(a, b)
                a = b + 1
                b = b + 9
        else:
            print((n // 2) + 1)
            print(1,2)
            a = 5
            b = 9
            for i in range(n // 2):
                print(a, b)
                a = b + 2
                b = b + 6