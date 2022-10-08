lst = list()
n = 1
while n:
    n = int(input())
    lst.append(n)
    
lst.pop()

for x in lst[::-1]:
    print(x)
    
