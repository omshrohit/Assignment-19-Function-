# write a python program to create a function that  finds a maximum of four numbers.
def maximum(num1,num2,num3,num4):
    list1=[num1,num2,num3,num4]
    print(max(list1))
maximum(10,4,3,5)


# another way
def maximum2(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        print(num1)
    elif num2>num1 and num2>num3 and num2>num4:
        print(num2)

    elif num3>num1 and num3>num2 and num3>num4:
        print(num3)
    else:
        print(num4)
maximum2(10,5,99,-100)