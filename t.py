def min_copper_coins(n):
    if n % 4 == 0:
        return n // 4
    return (n // 4) + 1

t = int(input())
for _ in range(t):
    n = int(input())
    result = min_copper_coins(n)
    print(result)

