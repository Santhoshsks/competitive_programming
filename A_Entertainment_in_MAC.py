for _ in range(int(input())):
    n = int(input())
    s = input()

    if s <= s[::-1]:
        print(s)
    else:
        print(s[::-1] + s)