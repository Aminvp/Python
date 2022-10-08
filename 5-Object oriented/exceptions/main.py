ls = [1, 2, 3, 4]
n = input()

try:
    print(ls[int(n)])
except IndexError:
    print('n is larger than ls size')
except ValueError as e:
    print(e)

