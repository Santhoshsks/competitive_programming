def exam(a, b): 
    if a % 2 == 0 and b % 2 == 0:
        return "YES"
    elif (a + (b * 2)) % 2 == 0 and a % 2 == 0 and a != 0:
        return "YES"
    else:
        return "NO"
    
for _ in range(int(input())):
    a, b = tuple(map(int, input().split()))
    print(exam(a,b))