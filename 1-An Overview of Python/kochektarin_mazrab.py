p, d = input().split()
p = int(p)
d = int(d)
i = 1
while True:
    x = d * i
    i += 1
    r = x % p
    q = p / 2
    if r <= q :
        break
print(x)
