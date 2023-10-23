inp = int(input())

def fibo(n):
    if n == 0:
        return [0,0,0]
    elif n == 1:
        return [0,0,1] 
    a = -1
    b = 1
    c = 0
    temp1 = 0
    temp2 = 0
    while c != n:
        temp1 = a
        temp2 = b
        c = a + b
        a = b
        b = c

    return [0] + [temp1, temp2]

print(" ".join(map(str, fibo(inp))))