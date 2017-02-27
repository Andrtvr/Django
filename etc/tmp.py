def double_it(func):
    def tmp(*args):
        return func(*args)*2
    return tmp

@double_it
def mult(a,b):
    return a*b



