def calc(a):
    avg = sum(a)/len(a)
    lst = sorted(a)
    size = int(len(lst))
    middle = int(len(lst))//2
    if size % 2 != 0:
        mid = lst[middle]
    else:
        mid = (lst[middle] + lst[middle-1])/2
    return avg, mid, max(a)
    
