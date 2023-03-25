# write a python program to multiply all the numbers in a list.

def multiply(list1):
    mult=1
    if len(list1)>0:
        for i in list1:
            mult*=i
        print(mult)
    else:
        print("empty List")
multiply([5,2,6,5])