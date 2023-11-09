n = int(input())

spaces = " " * ((n + 1) * 2) 
numbers = ""
print(f"{spaces}{numbers}{spaces}", end="")

for i in range(1, n + 2):
    spaces = " " * ((n + 1 - i) * 2) 
    numbers = " ".join(str(j) for j in range(i))
    print(f"{spaces}{numbers}{numbers[:-1][::-1]}{spaces}")


for i in range(n , -1, -1):
    spaces = " " * ((n + 1 - i) * 2) 
    numbers = " ".join(str(j) for j in range(i))
    print(f"{spaces}{numbers}{numbers[:-1][::-1]}{spaces}")

spaces = " " * ((n + 1) * 2) 
numbers = ""
print(f"{spaces}{numbers}{spaces}", end="")
