a = 100

def greet_someone(func_arg: int, *args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)
    global a
    print('a in greet_someone: ', a)
    print('func_arg in greet_someone: ', func_arg)

    a = 1000
    z = 10000
    print('a after modifying: ', a)
    def inner():
        global a
        print('first inner a: ', a)
        a = 10
        b = 20
        print('after modifying in inner: ', a)
    inner()
    print('outer func a: ', a)



print('first a: ', a)

greet_someone(a, 1, 2, 3, 4, func=True, bool_val=False, n=12.3)

print('last a: ', a)