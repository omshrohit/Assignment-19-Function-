#  write a python program to create a function  which excepts kwargs arguments

def func(**kwargs):

    for key,value in kwargs.items():
        print("%s : %s"%(key,kwargs[key]))

# function call

func(name="rohit",age="21",depart="CSE")