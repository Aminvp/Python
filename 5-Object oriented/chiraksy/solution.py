class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    ls = list()
    for func in func_ls:
        try:
            func()
        except Exception as e:
            msg = str(e)
            function = func
            ep = ExceptionProxy(msg, function)
            ls.append(ep)
        else:
            msg = "ok!"
            function = func
            ep = ExceptionProxy(msg, function)
            ls.append(ep)
    return ls

def f():
    1/0

def g():
    pass

tr_ls = transform_exceptions([f, g])

print(tr_ls)

for tr in tr_ls:
    print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)
