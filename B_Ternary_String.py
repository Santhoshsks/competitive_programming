for _ in range(int(input())):
    string = input()
    count_min = float('inf')
    for i in range(len(string)):
        for j in range(len(string)):
            flag = [0,0,0]
            for k in string[i:j+2]:
                if k == '1' and flag[0] == 0:
                    flag[0] = 1
                elif k == '2' and flag[1] == 0:
                    flag[1] = 1
                elif k == '3' and flag[2] == 0:
                    flag[2] = 1
            if sum(flag) == 3 and j - i + 2 < count_min:
                count_min = j - i + 2

    if count_min == float('inf'):
        print(0)
    else:
        print(count_min)