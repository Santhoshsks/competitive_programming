def min_chars_to_delete(t, test_cases):
    for n, s in test_cases:
        count = 0
        i = 0
        while i < len(s):
            if i + 2 < len(s) and (s[i:i+3] == "pie" or s[i:i+3] == "map"):
                count += 1
                i += 3  
            else:
                i += 1
        print(count)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

min_chars_to_delete(t, test_cases)
