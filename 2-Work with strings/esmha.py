n = int(input())
name = list()
ans = -1

for i in range(n):
    name += input().split()
print(name)

for n in name:
    t = ''
    for ch in n:
        if ch not in t:
            t += ch
    print(t)
    ans = max(ans, len(t))
    
print(ans)
print(t)    
    
        


        



    
    
            
        
        

            
        

