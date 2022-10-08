from datetime import datetime

def day_calculator(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    sajjad_bdate = datetime.strptime("1999-01-14",'%Y-%m-%d')
    days = (date - sajjad_bdate).days
    if days < 0:
        return('Not yet born')
    else:
        return(days)

