n = int(input())

for i in range(1, n + 2):
    spaces = " " * ((n + 1 - i) * 2) 
    numbers = " ".join(str(j) for j in range(i))
    print(f"{spaces}{numbers}{numbers[:-1][::-1]}")

for i in range(n , -1, -1):
    spaces = " " * ((n + 1 - i) * 2) 
    numbers = " ".join(str(j) for j in range(i))
    print(f"{spaces}{numbers}{numbers[:-1][::-1]}")