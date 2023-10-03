result = 0
for i in range(26, 0, -1):
    result += 1 / i

result *= 26
print("ans:", result)
