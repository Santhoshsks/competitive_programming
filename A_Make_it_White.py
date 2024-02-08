for _ in range(int(input())):
    n = int(input())
    s = input()
    f = s.index('B')
    s = s[::-1]
    e = s.index('B')
    print(n - e - f)
