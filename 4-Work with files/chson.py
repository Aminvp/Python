import ast
import json

n = int(input())

d = dict()

for i in range(n):
    inp = input()
    if inp.startswith('print'):
        var = inp[inp.find(' ')+1:inp.find('[')]
        key = inp[inp.find('[')+1:inp.find(']')]
        if '"' in key:
            key = key.replace('"', '')
            print(d[var][key])
        else:
            print(d[var][int(key)])
    else:
        var, data = map(str, inp.split(':='))
        var = var.strip()
        data = data.strip()
        if data.startswith('['):
            d[var] = ast.literal_eval(data)
        elif data.startswith('{'):
            d[var] = json.loads(data)
    


            
    

    
    




