for _ in range(int(input())):
    n = int(input())
    periods = list(map(int, input().split()))
    current_year = 0
    for i in range(n):
        sign_period = periods[i]
        sign_year = current_year + sign_period - (current_year % sign_period)
        current_year = sign_year
            
    print(current_year)