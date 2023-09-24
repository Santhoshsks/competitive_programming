for _ in range(int(input())):
    smallest = 10 ** 9 + 1
    sec_smallest = 10 ** 9 + 1
    ans = 0
    list_len = int(input())
    if list_len == 1:
        list(map(int, input().split()))
        print(min(list(map(int, input().split()))))
    else:
        for _ in range(list_len):
            n = int(input())
            arr = list(map(int, input().split()))
            arr.sort()
            if arr[0] < smallest:
                smallest = arr[0]
            if arr[1] < sec_smallest:
                sec_smallest = arr[1]
            ans += arr[1]
        print(ans + smallest - sec_smallest)