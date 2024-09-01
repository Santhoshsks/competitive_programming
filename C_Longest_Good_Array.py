def exam(l, r):
    if l == r:
        return 1
    add = 1
    while(l + add <= r):
        l += add
        add += 1
    return add
    
for _ in range(int(input())):
    a, b = tuple(map(int, input().split()))
    print(exam(a,b))