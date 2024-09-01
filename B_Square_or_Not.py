def exam(n, s):
    sq = str(n ** 0.5).split('.')
    if sq[1] == '0':
        if s == n * '1':
            if n in [1, 4]:
                return "Yes"
        else:
            i = 0
            count = 0
            while i < n:
                if s[i] == '1' and count > 0:
                    break
                if s[i] == '0':
                    count += 1
                i += 1
            if count == int(sq[0]) - 2:
                return "Yes"
    return "No"


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(exam(n, s))