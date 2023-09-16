for _ in range(int(input())):
    
    a, b, c = map(int,input().split())
    if a == b:
        if (a + b + c) % 2:
            print("First")
        else:
            print("Second")

    elif a > b:
        print("First")
    
    else:
        print("Second")