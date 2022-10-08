def f(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
    return fact

def comb(n, k):
    a = f(n) / (f(k) * f(n-k))
    return int(a)

print(comb(5,3))
