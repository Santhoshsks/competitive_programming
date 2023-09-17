for _ in range(int(input())):
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    sum = 0
    x = min(bx, cx)
    y = min(by, cy)

    if ax < bx and ax < cx:
        sum += x - ax
    
    if ax > bx and ax > cx:
        sum += ax - x

    if ay < by and ay < cy:
        sum += y - ay
    
    if ay > by and ay > cy:
        sum += ay - y

    print(sum + 1)
    