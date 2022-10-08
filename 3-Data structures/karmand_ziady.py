n = int(input())
d = dict()
count = 0
for i in range(n):
    x, y = map(str, input().split())
    d.setdefault(x, [])
    d[x].append(y)

l = 0    
for k, v in d.items():
    if len(v) > l:
        l = len(v)
    
print(l)
