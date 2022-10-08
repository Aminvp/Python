def calculator(n, m, ls):
    lst = list()
    subList = [ls[n:n+m] for n in range(0, len(ls), m)]
    for x in subList:
        lst.append(sum(x))
    print(lst)
    c = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            c += lst[i]
        else:
            c -= lst[i]
    return c


# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
