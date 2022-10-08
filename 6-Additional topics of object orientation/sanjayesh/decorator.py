def decorator(validator):
    def check_func(func):
        def ret(*args, **kwargs):
            test = validator(*args, **kwargs)
            if test:
                return func(*args, **kwargs)
            return "error"
        return ret
    return check_func