
def decor(func):
    def inner(x,y):
        x=x+20
        y=y+20
        z=func(x,y)
        return z
    return inner