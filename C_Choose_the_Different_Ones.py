def check_elements_possible(a, b, k):
    max_a, min_a = max(a), min(a)
    max_b, min_b = max(b), min(b)
    
    range_values = max(max_a, max_b) - min(min_a, min_b)
    
    if range_values >= k:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(check_elements_possible(a, b, k))
