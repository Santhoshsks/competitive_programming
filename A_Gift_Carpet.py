t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    name = 'vika'
    done = 0
    carpet = []

    for _ in range(a):
        carp = input()
        carpet.append(carp)

    col = 0
    while col < b and b > 3 and done < 4:
        for row in range(a):
            if carpet[row][col] == name[done]:
                done += 1
                break
        col += 1

    if done == 4:
        print('YES')
    else:
        print("NO")