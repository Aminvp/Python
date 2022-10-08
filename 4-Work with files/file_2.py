def solve(file_name):
	with open(file_name, "r") as f:
		ans = 0
		for line in f.readlines():
		    line = line.strip()
		    if line == '' or line[0] == '#':
		        continue
		    ans +=1
		return ans
