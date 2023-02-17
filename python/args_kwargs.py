def args_func(*args):
    for name in args:
        print(name)

def kwargs_func(**kwargs):
    for key,value in kwargs.items():
        print(key, value)
        
## call the args_func
args_func('John', 'Paul', 'George', 'Ringo')
##call the kawrgs_func
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
kwargs_func(name='John', surname='Lennon', age=40)                