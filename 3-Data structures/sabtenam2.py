def check_registration_rules(**kwargs):
    yes = []
    invalids = ['quera', 'codecup']
    for item in kwargs:
        if not item in invalids and len(item) > 3 and len(kwargs[item]) > 5 and not kwargs[item].isdigit():
            yes.append(item)
    return yes
