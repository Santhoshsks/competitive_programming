for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    f = 0
    l = n - 1
    fl = float('inf')
    flag = True
    while(l >= f and l > -1 and f < n):
        if arr[l] > arr[f] and arr[l] <= fl:
            fl = arr[l]
            l -= 1
        elif arr[f] > arr[l] and arr[f] <= fl:
            fl = arr[f]
            f += 1
        elif arr[f] == arr[l] and arr[f] <= fl:
            fl = arr[f]
            f += 1
            l -= 1
        else:
            flag = False
            break
        
    if flag:
        print('Yes')
    else:
        print('No')
            
