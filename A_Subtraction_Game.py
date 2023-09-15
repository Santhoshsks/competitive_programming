for _ in range(int(input())):
    
    a , b = map(int, input().split())
    if min(a,b) - 1 == 0:
        print(a + b)
    else:
        print(min(a,b) - 1)