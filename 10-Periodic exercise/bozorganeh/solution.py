def capitalize(names):
    ls = list()
    for x in names:
        if ' ' in x:
            l = x.split()
            for i in range(len(l)):
                l[i] = l[i].capitalize()
            x = ' '.join(l)
            ls.append(x)
        else: 
            ls.append(x.capitalize())
        
    return ls



print(capitalize(['ali', 'REYHANEH', 'aMIR', 'AMIR abbas', 'Fatemeh Zahra']))
