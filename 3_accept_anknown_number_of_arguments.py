# write a python program to create a function which expects an unknown number of arguments.
def fun(*p):
    lis=[e for e in p]
    print(lis)
fun(10,20,2,30)