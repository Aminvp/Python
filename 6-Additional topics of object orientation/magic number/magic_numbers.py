class Strint(int):
    def __init__(self, num):
        self.num = num
    
    def __lt__(self, other):
        x = str(self.num)
        y = str(other.num)
        if x[-1] < y[-1]:
            return True
        elif y[-1] < x[-1]:
            return False

    def __gt__(self, other):
        x = str(self.num)
        y = str(other.num)
        if x[-1] > y[-1]:
            return True
        return False

    def __le__(self, other):
        x = str(self.num)
        y = str(other.num)
        if x[-1] <= y[-1]:
            return True
        elif y[-1] <= x[-1]:
            return False

    def __ge__(self, other):
        x = str(self.num)
        y = str(other.num)
        if x[-1] >= y[-1]:
            return True
        elif y[-1] <= x[-1]:
            return False

    def __eq__(self, other):
        x = str(self.num)
        y = str(other.num)
        if x[-1] == y[-1]:
            return True
        return False

    def __ne__(self, other):
        x = str(self.num)
        y = str(other.num)
        if x[-1] != y[-1]:
            return True
        return False   

    def __add__(self, other):
        x = str(self.num)
        y = str(other.num)
        z = x + y
        if z.startswith('0'):
            z = z.lstrip('0')
            if z == "":
                return 0
        return int(z) 

    def __sub__(self, other):
        x = str(self.num)
        y = str(other.num)
        for m in y[::-1]:
            if x[-1] == m:
                x = x[:len(x)-1]
                if x == "":
                    x = 0
            else:
                raise Exception('The subtraction is not valid!')
        return int(x)


    def __len__(self):
        x = str(self.num)
        return len(x)

    def __call__(self):
        x = str(self.num)
        y = ""
        number = { '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
        for n in x:
            y += number[n]
        return y

ob1 = Strint(8439)
ob2 = Strint(843)
print(ob1 - ob2)