class Reverse:
    def __init__(self, data):
        self.data = data
        self.idx = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = self.data[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx -= 1
        return item
            
        
        


ls = [10, 20, 30]
for it in Reverse(ls):
    print(it)
print(ls)

