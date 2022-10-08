import re

def check_registration_rules(**kwargs):
    lst = list()
    for k, v in kwargs.items():
        if len(v) >= 6 and len(k) >= 4:
            if k != 'quera' and k != 'codecup':
                if v.isdigit() == False:
                    lst.append(k)
    return lst
                
