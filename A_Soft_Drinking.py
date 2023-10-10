l = list(map(int, input().split()))

gas = (l[1] * l[2]) / (l[6])
laim = (l[3] * l[4]) / l[0]
sol = l[5] / (l[7]) 

print(min(gas, laim, sol))

