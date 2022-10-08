def process(path):
    lines = csv_reader(path)
    with open("C:\\Users\\AMIN_vp\\Desktop\\ans.csv", "r+") as f:
        for line in f.readlines():
            print(line)
                
        
        

def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.rstrip().split(',')

    
  
