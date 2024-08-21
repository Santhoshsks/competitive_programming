for _ in range(int(input())):
    n = int(input())   
    f = True

    while(f):
        if n < 0:
            f = False
        elif n == 0:
            break
        elif n < 11:
            f = False
        else:
            for i in range(2, len(str(n)) + 1):
                temp = int('1' * i)
                if n >= temp :
                    
                    return 0
            return -1
    

    if ans + 1:
        print("YES")
    else:
        print("NO")