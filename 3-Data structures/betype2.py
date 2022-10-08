string=list(input())
resultList=[]

for i in string:
    if i=='=' and len(resultList) != 0:
        resultList.pop()
    elif i == '=' and len(resultList) == 0:
        continue
    else:
        resultList.append(i)
        
print(''.join(resultList))
