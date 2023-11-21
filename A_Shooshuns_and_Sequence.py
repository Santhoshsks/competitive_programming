n, k = map(int, input().split())
sequence = list(map(int, input().split()))

ans = 0
flag = 0

for i in range(n):
    if all(element == sequence[0] for element in sequence):
        flag = 1
    else:
        sequence.append(sequence[k - 1])
        sequence.pop(0)
        ans += 1

if flag == 1:
    print(ans)

else:
    print(-1)