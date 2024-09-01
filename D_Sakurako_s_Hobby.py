t = int(input())

for _ in range(t):
    n = int(input())  
    p = list(map(int, input().split()))  
    s = input().strip()  

    result = [0] * n
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            cycle = []
            current = i
            while not visited[current]:
                cycle.append(current)
                visited[current] = True
                current = p[current] - 1 
            black_count = sum(1 for x in cycle if s[x] == '0')

            for x in cycle:
                result[x] = black_count
    
    print(' '.join(map(str, result)))