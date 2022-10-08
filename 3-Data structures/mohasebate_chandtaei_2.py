def calc(a):
    avg = sum(a) / len(a)
    maxi = max(a)
    median = ''
    if len(a) % 2 == 0:
        index = len(a)//2
        median = sum(sorted(a)[index-1:index+1])/2
    else:
        median = sorted(a)[int(len(a)/2)]
    return (avg, median, maxi)
