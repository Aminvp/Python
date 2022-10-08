import re

def solve(path):
    ans = 0
    with open(path, "r") as f:
        while True:
            line = f.readline()
            print(line)
            if line == '':
                break
            elif re.match(r'^[\s]*#', line):
                continue
            elif re.match(r'^[\s]*\n', line):
                continue
            ans += 1
    return ans
        
