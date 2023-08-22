t = int(input())
for i in range(t):
    n = int(input())
    string = input()
    cost = 1
    maxi = 1
    for i in range(1,n):
        if string[i] != string[i-1]:
            cost = 1

        else:
            cost += 1
        
        maxi = max(maxi,cost)

    print(maxi+1)