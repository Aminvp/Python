import os

d = dict()
def explore(ttype, address):
    ls = list(os.walk(address))
    for l in ls:
        d[l[0]] = 0
        for t in l[2]:
            if "." in t and t.split('.')[-1].lower() == ttype.lower():
                d[l[0]] += 1

    for i in d.copy():
        if not d[i]:
          d.pop(i)

    return d


print(explore("jpg", "sample_test_media"))