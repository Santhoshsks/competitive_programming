def dis(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for _ in range(int(input())):
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    sum = dis(ax, bx, ay, by) + dis(ax, cx, ay, cy) - dis(bx, cx, by, cy)
    print(sum // 2 + 1)
    