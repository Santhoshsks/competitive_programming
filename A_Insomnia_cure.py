import math
def lcm_2(x, y):
    return x * y // math.gcd(x, y)

def lcm_3(x, y, z):
    return lcm_2(lcm_2(x, y), z)

def lcm_4(a, b, c, d):
    return lcm_2(lcm_2(lcm_2(a, b), c), d)

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

def count_divisible(x):
    return d // x

damaged_dragons = (
    count_divisible(k)
    + count_divisible(l)
    + count_divisible(m)
    + count_divisible(n)
    - count_divisible(lcm_2(k, l))
    - count_divisible(lcm_2(k, m))
    - count_divisible(lcm_2(k, n))
    - count_divisible(lcm_2(l, m))
    - count_divisible(lcm_2(l, n))
    - count_divisible(lcm_2(m, n))
    + count_divisible(lcm_3(k, l, m))
    + count_divisible(lcm_3(k, l, n))
    + count_divisible(lcm_3(k, m, n))
    + count_divisible(lcm_3(l, m, n))
    - count_divisible(lcm_4(k, l, m, n))
)

print(damaged_dragons)

