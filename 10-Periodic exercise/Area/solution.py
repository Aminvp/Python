import math

switcher = {
        "square": lambda x: x*x,
        "circle": lambda r: math.pi * r * r,
        "rectangle": lambda x, y: x * y,
        "triangle": lambda x, h: x * h * 0.5
 }


def get_func(ls):
    lst = list()
    for x in ls:
        lst.append(switcher[x])
    return lst

                
            


ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

print(ls[0](1))
print(ls[1](2))
print(ls[2](2, 4))
print(ls[3](4, 5))