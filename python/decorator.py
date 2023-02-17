def outerfunc(func):
    def innerfunc():
        print('I am inner function')
        func()
    return innerfunc

def simple():
    print('Just ordinary function')

decorated=outerfunc(simple)
decorated()
#output: 
#I am inner function
#Just ordinary function