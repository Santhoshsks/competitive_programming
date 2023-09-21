for _ in range(int(input())):
    ans = 0
    for i in range(10):
        a = input()
        for j in range(10):
            if a[j] == 'X':
                if i == 0 or j == 0 or i == 10 - 1 or j == 10 - 1:
                    ans += 1
                elif i == 1 or j == 1 or i == 10 - 2 or j == 10 - 2:
                    ans += 2
                elif i == 2 or j == 2 or i == 10 - 3 or j == 10 - 3:
                    ans += 3
                elif i == 3 or j == 3 or i == 10 - 4 or j == 10 - 4:
                    ans += 4
                elif i == 4 or j == 4 or i == 10 - 5 or j == 10 - 5:
                    ans += 5
    print(ans)