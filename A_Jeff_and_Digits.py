n = int(input())
cards = list(map(int, input().split()))
count_0 = cards.count(0)
count_5 = cards.count(5)
if count_0 == 0:
    print(-1)
else:
    total_sum = sum(cards)
    if count_5 - count_5 % 9 != 0:
        largest_number = "5" * (count_5 - count_5 % 9) + "0" * count_0
        print(largest_number)
    else:
        print(0)
