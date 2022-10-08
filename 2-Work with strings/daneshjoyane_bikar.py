import re

def solve(arr):
    if re.match(r'^[#\d]+ \+ [#\d]+ = [#\d]+$', arr):
        lst = re.split(' ', arr)
        even = list()
        
        for i in range(len(lst)):
            if i % 2 == 0:
                even.append(lst[i])
        
        if '#' in even[0]:
            x = even[0].replace("#","[0-9]*")
            y = int(even[2]) - int(even[1])
            y = str(y)
            if re.match('^'+x+'$', y):
                x = y
                return(x + ' + ' + even[1] + ' = ' + even[2])
            else:
                return '-1'
        elif '#' in even[1]:
            x = even[1].replace("#","[0-9]*")
            y = int(even[2]) - int(even[0])
            y = str(y)
            if re.match('^'+x+'$', y):
                x = y
                return(even[0] + ' + ' + x + ' = ' + even[2])
            else:
                return '-1'
        else:
            x = even[2].replace("#","[0-9]*")
            y = int(even[0]) + int(even[1])
            y = str(y)
            if re.match('^'+x+'$', y):
                x = y
                return(even[0] + ' + ' + even[1] + ' = ' + x)
            else:
                return '-1'
